#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from config import picard_dedup
from jbiot import log


def dedups(bam, prefix):
    bam_dedup = prefix + ".dedup.bam"
    #logFile = prefix + ".dedup.log"
    cmd = "java -jar %s INPUT=%s OUTPUT=%s REMOVE_DUPLICATES=true AS=true VALIDATION_STRINGENCY=SILENT M=%s " % (picard_dedup,bam,bam_dedup,prefix+'.MarkDuplicates.stat')
    #print cmd
    log.run('dedup bam', cmd)
    return bam_dedup


