#! /usr/bin/env python
import sys
import os
from jbiot import log
from jbiot import jbiotWorker
import xlwt
import json
cwd = os.path.dirname(os.path.abspath(__file__))
mapRate =os.path.join(cwd,'../statBams/mappingRateStat.py')
if not os.path.exists(mapRate):
    mapRate = 'mappingRateStat.py'
covFormat = os.path.join(cwd,'../statBams/covFormat.py')
if not os.path.exists(covFormat):
    covFormat = "covFormat.py"
nXplot = os.path.join(cwd,'../statBams/nX.r')
if not os.path.exists(nXplot):
    nXplot = "nX.r"


def arranger(parms):
    '''Arranging final results and generating report directory
    
    Args:
        parms (dict) : which has the following keys::

            {
                regionStats: a list, results of sambamba depth region
                baseStats  : a list, results of sambamba depth base
                sortStats  : a list, results of sort bams called by samtools flagstat
                dedupStats : a list, results of dedup bams called by samtools flagstat
                targetStats: a list, results of target bams called by samtools flagstat
                samples    : a list, prefixs of bams
            }

    Reruens:
        dict : ``{"templtJson":"templtParms"}``
    '''
    regionStats = parms['regionStats']
    baseStats = parms['baseStats']
    sstats = parms['sortStats']
    dstats = parms['dedupStats']
    tstats = parms['targetStats']
    samples = parms['samples']
    try:
        targetDir = parms['resultsDirectory']
    except:
        targetDir = './'
    mapDir = os.path.join(targetDir,'report/mapping')
    nXdir = os.path.join(mapDir, 'nX')
    mapStat = os.path.join(mapDir, 'mapStat')
    if not os.path.exists(nXdir):
        cmd = "mkdir -p %s" % nXdir
        log.run('mkdir', cmd)
    if not os.path.exists(nXdir):
        cmd = "mkdir -p %s" % mapStat
        log.run('mkdir', cmd)
    for region in regionStats:
        cmd = 'mv %s %s'%(region, mapStat)
        log.run('mv coverage stat files', cmd)
    mapRateFile = os.path.join(mapDir, "readsMappingRateStat.xlsx")
    cmd = "%s %s %s %s %s %s"%(mapRate, mapRateFile, '-'.join(sstats), '-'.join(dstats), '-'.join(tstats), '-'.join(samples))    
    log.run("mapping rate stats", cmd)
    
    meanCovFile = os.path.join(mapDir,"AllFile.mean.coverage.xlsx")
    cmd = "%s %s %s %s "%(covFormat, '-'.join(baseStats), meanCovFile, '-'.join(samples))
    log.run('bam coverage stats', cmd)
    
    nxs = []
    for sample in samples:
        f = sample+'.cov.txt'
        out1 = os.path.join(nXdir,sample + '.region.coverage.png')
        out2 = os.path.join(nXdir, sample + '.region.coverage.pdf')
        cmd = "%s %s %s %s" %(nXplot, f, os.path.join(nXdir,sample), sample)
        log.run('plot target region coverage rate', cmd)
        nxs.append(out1)

    templtParms = genTempltRendrParms(mapRateFile, meanCovFile, nxs)

    return {'templtJson':templtParms}


def genTempltRendrParms(mapRateFile, meanCovFile, nxs):
    out_dict = {}
    out_dict['mappingRateStat'] = mapRateFile
    out_dict['targetRegionCovStat'] = meanCovFile
    out_dict['nXimages'] = nxs
    outfile = "mapping_template.json"
    jstr= json.dumps(out_dict)
    cmd = "echo '%s' > %s "%(jstr, outfile)
    log.run('generate template json', cmd)
    return outfile


class ArrgeWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(arranger, params)
