#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(cwd,'../'))

try:
    from config import sambamba
except:
    sambamba = 'sambamba'
    picard = ''
from jbiot import log
from jbiot import jbiotWorker


def sorts(parms):
    '''sorting bam file
        
    Args:
        parms (dict) : which has the following keys::
        
            {
                bam   : bam file
                prefix: prefix of output
                args  : args of sambamba sort
            }
    
    Returns:
        dict : ``{"bam":"bam_sort", "prefix":"prefix"}``
    '''
    bam = parms['bam']
    prefix = parms['prefix']
    args = parms['args']
    bam_sort = prefix + ".sort.bam"
    cmd = "%s sort %s %s -o %s " % (sambamba,bam,args, bam_sort)
    log.run('sort bam', cmd)
    return {"bam":bam_sort, 'prefix': prefix}


class SortWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(sorts, params)


