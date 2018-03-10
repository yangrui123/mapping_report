import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from bamProcess import sorts, dedups, intersects, indexs


ref = "/lustre/common/genomes/human/hg19/bwa_index/ucsc.hg19.fasta"
bam = "/home/testData/mapping_report/data/tumor.map.raw.bam"
bed = "/home/testData/mapping_report/127.bed"

def test_bammer():
    prefix = "tumor"
    sort_parms = "tmpdir='./'"
    sort_outs = sorts.sorts({'bam':bam, 'prefix':prefix, 'args': sort_parms})
    dedup_outs = dedups.dedups(sort_outs)
    dedup_outs['bed'] = bed
    intersect_outs = intersects.intersects(dedup_outs)
    indexs.indexs(dedup_outs)
    indexs.indexs(intersect_outs)


if __name__ == '__main__':
    test_bammer()
