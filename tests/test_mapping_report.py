import sys, os
cwd = os.path.dirname(os.path.abspath(__file__))


fastqs = './data/fastqs.yaml'
parms = './data/parms.yaml'


def test_mapping():
   cmd = "python %s -i %s -c %s" %(os.path.join(cwd, '/lustre/users/yangrui/devwork/mapping_report/bin/mapping_report.py'), fastqs, parms)
   os.system(cmd)


if __name__ == '__main__':
    test_mapping()
