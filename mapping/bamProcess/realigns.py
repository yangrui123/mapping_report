#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

from config import GenomeAnalysisTK
from jbiot import log


def realigns(bam, prefix, ref, parms, mem_of_java):
    aln_list = prefix + ".list"
    realn_bam = prefix + ".realn.bam"
    cmd1 = "java -Xmx%s -jar %s -T RealignerTargetCreator %s -R %s -I %s -o %s -allowPotentiallyMisencodedQuals "% (mem_of_java,GenomeAnalysisTK,parms,ref, bam,aln_list)
    #cmd1 += ' 2>%s'%prefix+'.realn.log'
    cmd2 = "java -Xmx%s -jar %s -T IndelRealigner -R %s -I %s -targetIntervals %s -o %s -allowPotentiallyMisencodedQuals" % (mem_of_java,GenomeAnalysisTK, ref, bam,aln_list,realn_bam)
    #cmd2 += ' 2>>%s'%prefix+'.realn.log'
    #print cmd1
    log.run('realign', cmd1)
    #print cmd2
    log.run('realign', cmd2)
    return realn_bam
