#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from config import sambamba
from jbiot import log

def indexs(bam):
    cmd = "%s index %s" % (sambamba,bam)
    #print cmd
    log.run('bam index', cmd)
