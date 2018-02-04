#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sorts, dedups, stat, realigns, bqsr, intersects, indexs


class bamer:
    
    def __init__(self, ref, prefix):
        self.ref = ref
        self.prefix = prefix

    def sort_bam(self, bam, sort_parms):
        return sorts.sorts(bam, self.prefix, sort_parms)
    
    def dedup_bam(self, bam):
        return dedups.dedups(bam, self.prefix)

    def stat_bam(self, bam):
        return stat.basestat(bam, self.prefix)

    def realign_bam(self, bam, realign_parms, mem_of_java):
        return realigns.realigns(bam, self.prefix, self.ref, realign_parms, mem_of_java)

    def bqsr_bam(self, bam,bed, parms, mem_of_java):
        return bqsr.bqsr(bam, bed, self.prefix, mem_of_java, parms, self.ref)
        
    def intersect_bam(self, bam, bed):
        return intersects.intersects(bam, bed, self.prefix)

    def index_bam(self, bam):
        return indexs.indexs(bam)
