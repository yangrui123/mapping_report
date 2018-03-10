import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from arranger.arranger import arranger



def test_arranger():
    path = "/home/testData/mapping_report/data"
    sstats = [path+'tumor.sort.stat',path+'normal.sort.stat']
    dstats = [path+'tumor.dedup.stat', path+'normal.sort.stat']
    tstats = [path+'tumor.target.stat', path+'normal.target.stat']
    samples = ["tumor", "normal"]
    parms = {}
    parms['regionStats'] =  [path+'normal.coverage.base.txt', path+'tumor.coverage.base.txt']
    parms['baseStats'] = [path+'normal.coverage.base.txt', path+'tumor.coverage.base.txt']
    parms['sortStats'] = sstats
    parms['dedupStats'] = dstats
    parms['targetStats'] = tstats
    parms['samples'] = samples
    parms['suffix'] = 'cov.txt'
    arranger(parms)

if __name__ == '__main__':
    test_arranger()
