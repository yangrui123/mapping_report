import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from arranger.arranger import arranger


PATH = "/home/testData/mapping_report/data"

def test_arranger():
    parms = {}
    parms['regionStats'] =  [PATH+'normal.coverage.base.txt', PATH+'tumor.coverage.base.txt']
    parms['mapRateFile'] =  PATH+'readsMappingRateStat.xlsx'
    parms['meanCovFile'] = PATH+'AllFile.mean.coverage.xlsx'
    parms['nXs'] = []
    arranger(parms)


if __name__ == '__main__':
    test_arranger()
