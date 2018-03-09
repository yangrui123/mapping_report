import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from mapProcess.mapping import aligner


ref = "/lustre/common/genomes/human/hg19/bwa_index/ucsc.hg19.fasta"
fq1 = "/home/testData/mapping_report/tumor_R1.fq.gz"
fq2 = "/home/testData/mapping_report/tumor_R2.fq.gz"


def test_mapping():
    prefix = "tumor"
    parms = "-t 4"
    aln = aligner(fq1, fq2, ref, prefix, parms)
    bam = aln.align()


if __name__ == '__main__':
    test_mapping()
