#!/bin/python2.7
# coding:utf-8
__author__ = 'yangrui'

import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))

try:
    from config import intersectBed
except:
    intersectBed = "intersectBed"
from jbiot import log
from jbiot import jbiotWorker


def intersects(parms):
    bam = parms['bam']
    bed = parms['bed']
    prefix = parms['prefix']
    bam_target = prefix + ".target.bam"
    cmd = "%s -abam %s -b %s -wa -u > %s" % (intersectBed,bam,bed,bam_target)
    log.run('intersect bam', cmd)
    return {'bam':bam_target, 'prefix':prefix, 'bed':bed}


class IntrsctWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(intersects, params)

