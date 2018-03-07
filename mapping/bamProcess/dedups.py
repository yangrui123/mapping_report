#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

try:
    from config import picard_dedup
except:
    picard_dedup = 'MarkDuplicates.jar'
from jbiot import log
from jbiot import jbiotWorker


def dedups(parms):
    bam = parms['bam']
    prefix = parms['prefix']
    bam_dedup = prefix + ".dedup.bam"
    cmd = "java -jar %s INPUT=%s OUTPUT=%s REMOVE_DUPLICATES=true AS=true VALIDATION_STRINGENCY=SILENT M=%s " % (picard_dedup,bam,bam_dedup,prefix+'.MarkDuplicates.stat')
    log.run('dedup bam', cmd)
    return {'bam':bam_dedup, 'prefix': prefix}


