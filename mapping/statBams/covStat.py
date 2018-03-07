import sys,os
try:
    from config import sambamba
except:
    sambamba = 'sambamba'
from jbiot import log
from jbiot import jbiotWorker


def statCov(parms):
    bams = parms['bams']
    bed = parms['bed']
    region_outs = []
    base_outs = []
    for bam, prefix in bams:
        out = prefix + '.coverage.region.txt'
        cmd = "%s depth region -L %s %s -o %s"%(sambamba, bed, bam, out)
        log.run("stat coverage", cmd, para=2)
        region_outs.append(out)
        out = prefix + '.coverage.base.txt'
        cmd = "%s depth base -L %s %s -o %s"%(sambamba, bed, bam, out)
        log.run("stat coverage", cmd, para=2)
        base_outs.append(out)
    return {'regionStats':region_outs, 'baseStats':base_outs}


def uniqStat(bams):
    outs = []
    for bam in bams:
        cmd = ""
        log.run("stat unique mapped reads", cmd, para=2)
        outs.append(out)
    return outs


class StatCovWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(statCov, params)



