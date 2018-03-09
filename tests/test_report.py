import sys,os
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, '../mapping'))
from report.report import report



def test_report():
    report('mapping_template.json')    


if __name__ == '__main__':
    test_report()
