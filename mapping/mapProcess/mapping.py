#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import bwa 

class aligner:
    
    def __init__(self,fq1,fq2,reference,prefix,parms):
        self.fq1 = fq1
        self.fq2 = fq2
        self.ref = reference
        self.parms = parms
        self.prefix = prefix

    def align(self):
        bam = bwa.aln(self.fq1,self.fq2,self.prefix, self.ref, self.parms)
        return bam
