#! /usr/bin/env python
import sys
import os
try:
    from config import samtools
    from config import sambamba
except:
    samtools = 'samtools'
from jbiot import log
from jbiot import jbiotWorker


def statMappingRate(parms):
    '''statistic bam files
    
    Args:
        parms (dict) : which has the following keys::
        
            {
                bams   : a list, [[bam1, prefix1],[bam2, prefix2], ...]
                suffix : suffix of output files
            }

    Returns:
        dict : ``{"bamStats":"bam_stats"}``
    '''
    bams = parms['bams']
    suffix = parms['suffix']
    stats = []
    for bam, prefix in bams:
        out = prefix + '.'+ suffix
        cmd = "%s flagstat %s > %s"%(samtools, bam, out)
        log.run("mapping stat", cmd, para=2)
        stats.append(out)
    return {'bamStats':stats}


class StatMapRate(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(statMappingRate, parms)


