import sys
import os
import yaml

cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd,'../'))
from mapping.mapProcess.mapping import aligner
from mapping.bamProcess.bamer import bamer


def mapping(fq_dict, ref, map_parms):
    bams = []
    for sample in fq_dict.keys():
        fqs = fq_dict[sample]
        fq1, fq2 = fqs[0][0], fqs[1][0]
        aln = aligner(fq1,fq2,ref,sample,map_parms)
        bam = aln.align()
        bams.append([bam, sample])
    return bams


def bammer(bams,ref, bed, mem_of_java, sort_parms, realign_parms, bqsr_parms):
    dedupBams = []
    sortBams = []
    targetBams = []
    samples = []
    for bam, sample in bams:
        bm = bamer(ref,sample)
        bam_sort = bm.sort_bam(bam,sort_parms)
        bam_dedup = bm.dedup_bam(bam_sort)
        #bam_stat = bm.stat_bam(bam_dedup)
        #bam_realign = bm.realign_bam(bam_dedup, realign_parms, mem_of_java)
        bam_target = bm.intersect_bam(bam_dedup, bed)
        bam_index = bm.index_bam(bam_dedup) 
        bm.index_bam(bam_target)
        #bam_bqsr = bm.bqsr_bam(bam_dedup,bed,bqsr_parms, mem_of_java)
        dedupBams.append([bam_dedup, sample])
        sortBams.append([bam_sort, sample])
        targetBams.append([bam_target, sample])
        samples.append(sample)
    return sortBams, dedupBams, targetBams, samples


def reportArrge(sbams, dbams, tbams, ref, bed, samples, targetDir):
    from mapping.statBams.mappingStat import statMappingRate, statCov
    from mapping.arranger.arranger import arranger
    from mapping.report.report import report
    sstats = statMappingRate(sbams, '.sort.mapping.stat')
    dstats = statMappingRate(dbams, '.dedup.mapping.stat')
    tstats = statMappingRate(tbams, '.target.mapping.stat')    
    covs = statCov(tbams, bed)
    templtParms = arranger(targetDir, sstats, dstats, tstats, covs, samples)
    report(templtParms)


if __name__ == '__main__':
    usage = '''
Usage:
    mapping_report.py [-h | --help]
    mapping_report.py -i <input>  -c <parameter>

Options:
    -h --help
    -i input --input=input          fastq file, yamal format
    -c parms --parameter=parms      parameters
'''

    from docopt import docopt
    args = docopt(usage)
    fqYaml = args['--input']
    parmYaml = args['--parameter']
    infp = open(fqYaml,'a+')
    fq_dict = yaml.load(infp.read())['fastqs']
    pafp = open(parmYaml, 'r')
    parms_dict = yaml.load(pafp.read())
    ref = parms_dict['reference']
    map_parms = parms_dict['map']
    bed = parms_dict['bed']
    mem_of_java = parms_dict['mem_of_java']
    sort_parms = parms_dict['sort']
    realign_parms = parms_dict['realign']
    bqsr_parms = parms_dict['bqsr']    
    bams = mapping(fq_dict, ref, map_parms)
    sbams, dbams, tbams, samples = bammer(bams, ref, bed, mem_of_java, sort_parms, realign_parms, bqsr_parms)
    targetDir = parms_dict['resultsDirectory']
    reportArrge(sbams, dbams, tbams, ref, bed, samples, targetDir)
    infp.write('bams:\n')
    for i in range(len(dbams)):
        infp.write('    '+samples[i]+':'+' '+dbams[i][0]+'\n')
    infp.close()    
        

