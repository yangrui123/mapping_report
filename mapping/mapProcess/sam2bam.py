#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))
from config import samtools
from jbiot import log


def sam2bam(sam, prefix):
    bam = prefix + '.raw.bam'
    cmd = "%s view -bS %s > %s" % (samtools,sam,bam)
    #print cmd
    tag = "sam2bam"
    log.run(tag,cmd)
    return bam



