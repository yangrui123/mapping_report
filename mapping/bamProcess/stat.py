#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from config import bedtools
from jbiot import log


def basestat(bam,prefix):
    out = prefix + ".basedepth.txt"
    cmd = "%s genomecov -bga -split -ibam %s > %s" % (bedtools,bam,out)
    cmd2 = "gzip %s" % out
    #print cmd
    log.run('genomecov', cmd)
    #print cmd2
    log.run('gzip geonmecov', cmd2)
    return out
