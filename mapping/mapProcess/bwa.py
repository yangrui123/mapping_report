#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys,os
from sam2bam import sam2bam 
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))
from config import bwa
from jbiot import log


def aln(fq1, fq2, prefix, ref, parms):
    """bwa aligner
    
    Args:
        fq1 (str): the first fastq file
        fq2 (str): the second fastq file
        prefix (str): prefix of output file
        ref_bwa (str): reference file for bwa
        threads (str/int): threads for bwa
 
    Returns:
        bam (str): bam filename  
    """
    if fq2:
        sam = DoubleQ(fq1, fq2, prefix, ref, parms)
    else:
        sam = SingleQ(fq1, prefix, ref, parms)
    bam = sam2bam(sam, prefix+'.bwa')
    return bam


def DoubleQ(fq1, fq2, prefix,ref, parms):
    sam = prefix + ".bwa.raw.sam"
    #logFile = prefix + ".bwa.align.log"
    cmd = '%s mem %s -R "@RG\\tID:%s\\tSM:%s\\tLB:%s\\tPL:ILLUMINA" %s %s %s > %s ' % (bwa,parms, prefix,prefix,prefix,ref,fq1,fq2,sam)
    #print cmd
    tag = "bwa mem"
    log.run(tag,cmd)
    return sam


def SingleQ(fq1, prefix, ref, parms):
    sam = prefix + ".bwa.raw.sam"
    cmd = '%s mem %s -R "@RG\\tID:%s\\tSM:%s\\tLB:%s\\tPL:ILLUMINA" %s %s  > %s ' % (bwa,parms,prefix,prefix,prefix,ref,fq1,sam)
    #print cmd
    tag = "bwa mem"
    log.run(tag,cmd)
    return sam

