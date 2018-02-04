#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from config import intersectBed
from jbiot import log


def intersects(bam, bed, prefix):
    bam_target = prefix + ".target.bam"
    cmd = "%s -abam %s -b %s -wa -u > %s" % (intersectBed,bam,bed,bam_target)
    #print cmd
    log.run('intersect bam', cmd)
    return bam_target

