import sys, os
import config
from jbiot import log
import xlwt
import json
cwd = os.path.dirname(os.path.abspath(__file__))
mapRate =os.path.join(cwd,'../statBams/mappingRateStat.py')
covStat = os.path.join(cwd,'../statBams/covStat.py')
nXplot = os.path.join(cwd,'../statBams/nX.r')


def arranger(targetDir, sstats, dstats, tstats, covs, samples, suffix=".cov.txt"):
    mapDir = os.path.join(targetDir,'mapping')
    nXdir = os.path.join(mapDir, 'nX')
    mapStat = os.path.join(mapDir, 'mapStat')
    if not os.path.exists(nXdir):
        cmd = "mkdir -p %s" % nXdir
        log.run(cmd, cmd)
    if not os.path.exists(nXdir):
        cmd = "mkdir -p %s" % mapStat
        log.run(cmd, cmd)
    mapRateFile = os.path.join(mapDir, "readsMappingReateStat.xlsx")
    cmd = "python %s %s %s %s %s %s"%(mapRate, mapRateFile, '-'.join(sstats), '-'.join(dstats), '-'.join(tstats), '-'.join(samples))    
    log.run("mapping rate stats", cmd)
    
    meanCovFile = os.path.join(mapDir,"AllFile.mean.coverage.xlsx")
    cmd = "python %s %s %s %s %s "%(covStat, '-'.join(covs), meanCovFile, '-'.join(samples), suffix)
    log.run('bam coverage stats', cmd)
    
    nxs = []
    for sample in samples:
        f = sample+suffix
        out1 = os.path.join(nXdir,sample + '.region.coverage.png')
        out2 = os.path.join(nXdir, sample + '.region.coverage.pdf')
        cmd = "Rscript %s %s %s %s" %(nXplot, f, os.path.join(nXdir,sample), sample)
        log.run('plot target region coverage rate', cmd)
        nxs.append(out1)

    templtParms = genTempltRendrParms(mapRateFile, meanCovFile, nxs)

    return templtParms


def genTempltRendrParms(mapRateFile, meanCovFile, nxs):
    out_dict = {}
    out_dict['mappingRateStat'] = mapRateFile
    out_dict['targetRegionCovStat'] = meanCovFile
    out_dict['nXimages'] = nxs
    outfile = "TempltRendrParms.json"
    fwp = open(outfile, 'w')
    fwp.write(json.dumps(out_dict))
    fwp.close()
    return outfile



