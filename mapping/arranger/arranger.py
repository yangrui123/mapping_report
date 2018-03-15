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
                mapRateFile: statistics of BAM mapping information
                meanCovFile: summary of mean coverage for bams
                nXs        : a list, plots of bam coverage
            }   

    Reruens:
        dict : ``{"templtJson":"templtParms"}``
    '''
    regionStats = parms['regionStats']
    mapRateFile = parms['mapRateFile']
    meanCovFile = parms['meanCovFile']
    nxs = parms['nXs']
    mapDir = 'report/mapping'
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
        self.execMyfunc(arranger, params)
