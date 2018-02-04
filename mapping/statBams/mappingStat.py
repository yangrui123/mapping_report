import sys,os
import xlwt
from config import samtools
from jbiot import log
from config import sambamba



def statMappingRate(bams, suffix):
    stats = []
    for bam, prefix in bams:
        out = prefix + suffix
        cmd = "%s flagstat %s > %s"%(samtools, bam, out)
        log.run("mapping stat", cmd, para=2)
        stats.append(out)
    return stats


def statCov(bams, bed):
    outs = []
    for bam, prefix in bams:
        out = prefix + '.coverage.txt'
        cmd = "%s depth region -L %s %s -o %s"%(sambamba, bed, bam, out)
        log.run("stat coverage", cmd, para=2)
        outs.append(out)
    return outs


def uniqStat(bams):
    outs = []
    for bam in bams:
        cmd = ""
        log.run("stat unique mapped reads", cmd, para=2)
        outs.append(out)
    return outs
