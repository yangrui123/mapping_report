#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))
try:
    from config import bwa
    from config import samtools
except:
    bwa = 'bwa'
    samtools = 'samtools'
from jbiot import log
from jbiot import jbiotWorker


def aln(parms):
    """bwa aligner
    
    Args:
        parms (dict) : which has the following keys:: 

            {
                fq1      : the first fastq file
                fq2      : the second fastq file
                prefix   : prefix of output file
                reference: reference file for bwa
                args     : extra args for map
            }
 
    Returns:
        dict: ``{"bam":"bam_file"}``
    """
    fq1 = parms['fq1']
    fq2 = parms['fq2']
    prefix = parms['prefix']
    ref = parms['reference']
    args = parms['args']
    if fq2:
        sam = DoubleQ(fq1, fq2, prefix, ref, args)
    else:
        sam = SingleQ(fq1, prefix, ref, args)
    bam = prefix+'.bam'
    cmd = "%s view -bS %s > %s" %(samtools, sam, bam)
    log.run('sam to bam', cmd)
    return {'bam':bam}


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


def BwaWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(aln, params)
