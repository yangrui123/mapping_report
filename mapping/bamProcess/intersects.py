#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(cwd,'../'))

try:
    from config import intersectBed
except:
    intersectBed = "intersectBed"
from jbiot import log
from jbiot import jbiotWorker


def intersects(parms):
    '''intersect bam with bed file
    
    Args:
        parms (dict) : which has the following keys::
        
            {
                bam   : bam file
                bed   : bed file
                prefix: prefix of output
            }
    
    Returns:
        dict : ``{"bam":"bam_target", "prefix":"prefix", "bed":"bed"}``
    '''
    bam = parms['bam']
    bed = parms['bed']
    prefix = parms['prefix']
    bam_target = prefix + ".target.bam"
    cmd = "%s -abam %s -b %s -wa -u > %s" % (intersectBed,bam,bed,bam_target)
    log.run('intersect bam', cmd)
    return {'bam':bam_target, 'prefix':prefix, 'bed':bed}


class IntrsctWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(intersects, params)

