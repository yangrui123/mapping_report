import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from mapProcess.bwa import aln


ref = "/lustre/common/genomes/human/hg19/bwa_index/ucsc.hg19.fasta"
fq1 = "/home/testData/mapping_report/tumor_R1.fq.gz"
fq2 = "/home/testData/mapping_report/tumor_R2.fq.gz"


def test_mapping():
    prefix = "tumor"
    bwa_args = "-t 4"
    inputs = {'fq1':fq1, 'fq2':fq2, 'reference':ref, 'args':bwa_args, 'prefix':prefix}
    res = aln(inputs)


if __name__ == '__main__':
    test_mapping()
