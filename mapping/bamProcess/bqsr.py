#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from config import GenomeAnalysisTK
from indexs import indexs
from jbiot import log


def bqsr(bam, bed, prefix, mem_of_java, parms, ref):
    #if not os.path.exists(bam+'.bai'):
     #   indexs(bam)    
    grp = prefix + ".grp"
    grp_bam = prefix + ".bqsr.bam"
    cmd1 = "java -Xmx%s -jar %s -T BaseRecalibrator -R %s  %s -I %s -o %s " % (mem_of_java,GenomeAnalysisTK,ref,parms,bam,grp)
    if bed:
        cmd1 += "-L %s "%(bed)
    cmd2 = "java -Xmx%s -jar %s -T PrintReads -R %s %s -I %s -BQSR %s -o %s "% (mem_of_java,GenomeAnalysisTK,ref,parms,bam,grp,grp_bam)
    #print cmd1
    log.run('bqsr', cmd1)
    #print cmd2
    log.run("bqsr", cmd2)
    return grp_bam
