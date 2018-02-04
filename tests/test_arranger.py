import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from arranger.arranger import arranger



def test_arranger():
    targetDir = "./"
    sstats = ['tumor.sort.stat','normal.sort.stat']
    dstats = ['tumor.dedup.stat', 'normal.sort.stat']
    tstats = ['tumor.target.stat', 'normal.target.stat']
    covs = ['tumor.cov.txt','normal.cov.txt']
    samples = ["tumor", "normal"]
    arranger(targetDir, sstats, dstats, tstats, covs, samples)

if __name__ == '__main__':
    test_arranger()
