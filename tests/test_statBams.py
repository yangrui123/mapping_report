import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from statBams.mappingStat import statMappingRate


PATH = "/home/testData/mapping_report/data"

def test_statBams():
    parms = {}
    parms['sortBams'] = [[PATH+'normal.sort.bam', 'normal']]
    parms['dedupBams'] = [[PATH+'normal.dedup.bam', 'normal']]
    parms['targetBams'] = [[PATH+'normal.target.bam', 'normal']]
    parms['bed'] = '/home/testData/mapping_report/127.bed'
    parms['samples'] = ['normal']
    statMappingRate(parms)


if __name__ == '__main__':
    test_statBams()
