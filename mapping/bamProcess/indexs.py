#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

import sys
import os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(cwd,'../'))

try:
    from config import sambamba
except:
    sambamba = 'sambamba'
from jbiot import log
from jbiot import jbiotWorker


def indexs(parms):
    '''index bam
    
    Args:
        parms (dict) : which has the following keys::
        
            {
                bam: bam file
            }

    Returns: null
    '''
    bam = parms['bam']
    cmd = "%s index %s" % (sambamba,bam)
    log.run('bam index', cmd)


class IndxWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(indexs, params)
