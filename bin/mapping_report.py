#! /usr/bin/env python
import sys
import os
import yaml

cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(cwd,'../'))
from mapping.mapProcess.bwa import aln
from mapping.bamProcess import sorts, dedups, intersects, indexs
try:
    import config
except:
    pass
from jbiot import jbiotWorker


def mapping(parms):
    fq_dict = parms['fastqs']
    ref = parms['reference']
    map_args = parms['bwa_args']
    bams = []
    for sample in fq_dict.keys():
        fqs = fq_dict[sample]
        fq1, fq2 = fqs[0][0], fqs[1][0]
        inputs = {'fq1':fq1, 'fq2':fq2, 'reference':ref, 'args':map_args, 'prefix':str(sample)}
        bam = aln(inputs)['bam']
        bams.append([bam, sample])
    parms['bams'] = bams
    return parms


def bammer(parms):
    bams = parms['bams']
    dedupBams = []
    sortBams = []
    targetBams = []
    samples = []
    for bam, sample in bams:
        sort_outs = sorts.sorts({'bam':bam, 'prefix':str(sample), 'args': parms['sambamba_sort_args']})
        dedup_outs = dedups.dedups(sort_outs)
        dedup_outs['bed'] = parms['bed']
        intersect_outs = intersects.intersects(dedup_outs)
        indexs.indexs(dedup_outs) 
        indexs.indexs(intersect_outs)
        dedupBams.append([dedup_outs['bam'], str(sample)])
        sortBams.append([sort_outs['bam'], str(sample)])
        targetBams.append([intersect_outs['bam'], str(sample)])
        samples.append(str(sample))
    return {'sortBams':sortBams, 'dedupBams':dedupBams, 'targetBams':targetBams, 'samples':samples, 'bed':parms['bed'], 'reference':parms['reference']}



def statBam(parms):
    from mapping.statBams.mappingStat import statMappingRate
    covs = statMappingRate(parms)
    return covs



def reportArrge(parms):
    from mapping.arranger.arranger import arranger
    from mapping.report.report import report
    outs = arranger(parms)
    outs['template'] = parms['template']
    report(outs)



def writeYaml(parms):
    parmYaml = parms['parmYaml']
    fp = open(parmYaml, 'r')
    context = fp.read()
    fp.close()
    fwp = open(parmYaml, 'w')
    fwp.write(context) 
    bams = parms['bams']
    fwp.write('bams:\n')
    for bam in bams:
        fwp.write('    '+bam[1]+': '+bam[0]+'\n')
    fwp.close()    
    
 

def main(parms):
    map_outs = mapping(parms)  
    bam_outs = bammer(map_outs)  
    outs = statBam(bam_outs)
    outs['template'] = parms['mapping_template']
    reportArrge(outs)
    parms['bams'] = bam_outs['dedupBams']
    writeYaml(parms)


class MappingWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(main, params)


if __name__ == '__main__':
    usage = '''
Usage:
    mapping_report.py -c <parameter>

Options:
    -h --help
    -c,--conf <parameter>     parameters with yaml format
'''

    from docopt import docopt
    args = docopt(usage)
    parmYaml = args['--conf']
    parms = yaml.load(open(parmYaml, 'r'))
    parms['parmYaml'] = parmYaml
    main(parms)

