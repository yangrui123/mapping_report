import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))


parms = 'parms.yaml'


def test_mapping():
   cmd = "python %s -c %s" %(os.path.join(cwd, '/lustre/users/yangrui/devwork/mapping_report/bin/mapping_report.py'), parms)
   os.system(cmd)


if __name__ == '__main__':
    test_mapping()
