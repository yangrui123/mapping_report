import sys, os
import config
import xlwt
import json


def covStat(cov, outfile):
    import pandas as pd
    data = pd.read_table(covs[i], header=0, encoding='utf8')
    fwp = open(outfiles[i],'w')
    nx_list = []
    total = float(data.shape[0])
    for x in range(0,max_count):
        if x % 10 == 0:
            nx = len(data[data['meanCoverage']>=x])
            fwp.write('\t'.join(['>='+str(x), str(nx/total)]))
            fwp.write('\n')
    fwp.close()
    

if __name__ == '__main__':
    cov = sys.argv[2]
    outfile = sys.argv[3]
    cov = covStat(cov, outfile)

