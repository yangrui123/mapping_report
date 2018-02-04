import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from bamProcess.bamer import bamer


ref = "/lustre/common/genomes/human/hg19/bwa_index/ucsc.hg19.fasta"
bam = "tumor.map.raw.bam"
bed = "/home/testData/genomic/127.bed"

def test_bammer():
    prefix = "tumor"
    sort_parms = "tmpdir='./'"
    bm = bamer(ref, prefix)
    bam_sort = bm.sort_bam(bam, sort_parms)
    bam_dedup = bm.dedup_bam(bam_sort)
    bam_target = bm.intersect_bam(bam_dedup, bed)
    bm.index_bam(bam_dedup)
    bm.index_bam(bam_target)


if __name__ == '__main__':
    test_bammer()
