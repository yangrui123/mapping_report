#! /usr/bin/env python
import sys
import os
try:
    from config import samtools
    from config import sambamba
except:
    samtools = 'samtools'
    sambamba = 'sambamba'

cwd = os.path.dirname(os.path.abspath(__file__))
mapRate =os.path.join(cwd,'../statBams/mappingRateStat.py')
if not os.path.exists(mapRate):
    mapRate = '/opt/mappingRateStat.py'
covFormat = os.path.join(cwd,'../statBams/covFormat.py')
if not os.path.exists(covFormat):
    covFormat = "/opt/covFormat.py"
nXplot = os.path.join(cwd,'../statBams/nX.r')
if not os.path.exists(nXplot):
    nXplot = "/opt/nX.r"

from jbiot import log
from jbiot import jbiotWorker


def flagstat(bams, suffix):
    stats = []
    for bam, prefix in bams:
        out = prefix + '.'+ suffix
        cmd = "%s flagstat %s > %s"%(samtools, bam, out)
        log.run("mapping stat", cmd, para=2)
        stats.append(out)
    return stats



def statCov(bams, bed):
    region_outs = []
    base_outs = []
    for bam, prefix in bams:
        out = prefix + '.coverage.region.txt'
        cmd = "%s depth region -L %s %s -o %s"%(sambamba, bed, bam, out)
        log.run("stat coverage", cmd, para=2)
        region_outs.append(out)
        out = prefix + '.coverage.base.txt'
        cmd = "%s depth base -L %s %s -o %s"%(sambamba, bed, bam, out)
        log.run("stat coverage", cmd, para=2)
        base_outs.append(out)
    return region_outs,base_outs


def statMappingRate(parms):
    '''statistic bam files
    
    Args:
        parms (dict) : which has the following keys::
        
            {
                sortBams   : a list, [[bam1, prefix1],[bam2, prefix2], ...]
                dedupBams  : a list, [[bam1, prefix1],[bam2, prefix2], ...]
                targetBams : a list, [[bam1, prefix1],[bam2, prefix2], ...]
                bed        : bed file
                samples    : a list, prefixs of bams
            }

    Returns:
        dict : ``{"regionStats": "region_covs", "mapRateFile":"mapRateFile", "meanCovFile":"meanCovFile", "nXs": "nxs"}``
    '''
    sortbams = parms['sortBams']
    dedupbams = parms['dedupBams']
    targetbams = parms['targetBams']
    bed = parms['bed']
    samples = parms['samples']
    sstats = flagstat(sortbams, 'sort.mapping.stat')
    dstats = flagstat(dedupbams, 'dedup.mapping.stat')
    tstats = flagstat(targetbams, 'target.mapping.stat')
    region_covs, base_covs = statCov(dedupbams, bed)
    mapDir = 'report/mapping'
    nXdir = 'report/mapping/nX'
    mapRateFile = os.path.join(mapDir, "readsMappingRateStat.xlsx")
    cmd = "%s %s %s %s %s %s"%(mapRate, mapRateFile, '-'.join(sstats), '-'.join(dstats), '-'.join(tstats), '-'.join(samples))
    log.run("mapping rate stats", cmd)

    meanCovFile = os.path.join(mapDir,"AllFile.mean.coverage.xlsx")
    cmd = "%s %s %s %s "%(covFormat, '-'.join(base_covs), meanCovFile, '-'.join(samples))
    log.run('bam coverage stats', cmd)

    nxs = []
    for sample in samples:
        f = sample+'.cov.txt'
        out1 = os.path.join(nXdir,sample + '.region.coverage.png')
        out2 = os.path.join(nXdir, sample + '.region.coverage.pdf')
        cmd = "%s %s %s %s" %(nXplot, f, os.path.join(nXdir,sample), sample)
        log.run('plot target region coverage rate', cmd)
        nxs.append(out1)

    res = {'regionStats': region_covs, 'mapRateFile':mapRateFile, 'meanCovFile':meanCovFile, 'nXs': nxs}
    return res



class StatMapRate(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(statMappingRate, parms)


