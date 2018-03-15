#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(cwd,'../'))

try:
    from config import picard_dedup
except:
    picard_dedup = '/opt/MarkDuplicates.jar'
from jbiot import log
from jbiot import jbiotWorker


def dedups(parms):
    '''dedup bam
        
    Args:
        parms (dict) : which has the following keys::
        
            {
                bam   : bam file
                prefix: prefix of output
            }
    
    Returns:
        dict : ``{"bam":"bam_dedup", "prefix":"prefix"}``
    '''
    bam = parms['bam']
    prefix = parms['prefix']
    bam_dedup = prefix + ".dedup.bam"
    cmd = "java -jar %s INPUT=%s OUTPUT=%s REMOVE_DUPLICATES=true AS=true VALIDATION_STRINGENCY=SILENT M=%s " % (picard_dedup,bam,bam_dedup,prefix+'.MarkDuplicates.stat')
    log.run('dedup bam', cmd)
    return {'bam':bam_dedup, 'prefix': prefix}


class DupWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(dedups, params)
