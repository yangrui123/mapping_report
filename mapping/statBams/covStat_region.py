import sys, os
import config
import xlwt
import json


def covStat(covs, samples, outfile, suffix):
    import pandas as pd
    fwp = xlwt.Workbook()
    sheet1 = fwp.add_sheet('sheet1', cell_overwrite_ok=True)
    head = ["Sample", 'Target region mean coverage', 'Std']
    for i in range(len(head)):
        sheet1.write(0,i,head[i]) 
    for i in range(len(covs)):
        data = pd.read_table(covs[i], header=0, encoding='utf8')
        meanCov = '%.2f'%(data['meanCoverage'].mean())
        std = '%.2f'%(data['meanCoverage'].std())
        tmp = [samples[i], meanCov, std]
        for j in range(len(tmp)):
            sheet1.write(i+1, j, tmp[j])
        max_count = int(data['meanCoverage'].max()) 
        fwp2 = open(samples[i]+suffix, 'w')
        nx_list = []
        total = float(data.shape[0])
        nxs = []
        for x in range(0,max_count):
            if x % 10 == 0:
                nx = len(data[data['meanCoverage']>=x])
                nxs.append([x,nx])
        for i in range(min(50, len(nxs))):
            nx = nxs[i][1]
            x = nxs[i][0]
            fwp2.write('\t'.join(['>='+str(x), str(nx/total)]))
            fwp2.write('\n')
        fwp2.close()
    fwp.save(outfile)
    

if __name__ == '__main__':
    covs = sys.argv[1]
    outfile = sys.argv[2]
    samples = sys.argv[3]
    suffix = sys.argv[4]
    samples = samples.split('-')
    covs = covs.split('-')
    covStat(covs, samples, outfile, suffix)

