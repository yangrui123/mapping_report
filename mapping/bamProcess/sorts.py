#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from config import sambamba
from config import picard 
from jbiot import log


def sorts(bam, prefix, parms):
    bam_sort = prefix + ".sort.bam"
    cmd = "%s sort %s %s -o %s " % (sambamba,bam,parms, bam_sort)
    #print cmd
    log.run('sort bam', cmd)
    return bam_sort


def reorderBAM(bam, prefix, ref):
    bam_sort = prefix + ".reorder.bam"
    cmd = "java -jar %s ReorderSam I=%s O=%s REFERENCE=%s"%(picard, bam, bam_sort, ref)
    log.run('reorder bam', cmd)
    return bam_sort


if __name__ == '__main__':
    bam = sys.argv[1]
    prefix = sys.argv[2]
    ref = sys.argv[3]
    reorderBAM(bam, prefix, ref)
