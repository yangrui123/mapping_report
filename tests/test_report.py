import sys
import os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from report.report import report



def test_report():
    parms = {'templtJson':'/home/testData/mapping_report/data/mapping_template.json', 'template':'/home/testData/mapping_report/mapping_template.md'}
    res = report(parms)    


if __name__ == '__main__':
    test_report()
