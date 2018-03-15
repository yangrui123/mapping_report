#!/usr/bin/env python

import sys
import os
try:
    import config
except:
    pass
import xlwt
import pandas as pd
from jbiot import jbiotWorker


def MeanCovStat(parms):
    '''statistic base coverage of each site
        
    Args:
        parms (dict) : which has the following keys::
            
            {
                covs   : outputs of "sambamba depth base"
                samples: prefixs of covs
                outfile: output of mean coverage for each sample
            }

    Rerutns:
        dict : ``{"meanCovStat":"outfile"}``
    '''
    covs = parms['covs']
    samples = parms['samples']
    outfile = parms['outfile']
    fwp = xlwt.Workbook()
    sheet1 = fwp.add_sheet('sheet1', cell_overwrite_ok=True)
    head = ["Sample", 'Target region mean coverage', 'Std']
    for i in range(len(head)):
        sheet1.write(0,i,head[i]) 
    for i in range(len(covs)):
        data = pd.read_table(covs[i], header=0, encoding='utf8')
        meanCov = '%.2f'%(data['COV'].mean())
        std = '%.2f'%(data['COV'].std())
        tmp = [samples[i], meanCov, std]
        for j in range(len(tmp)):
            sheet1.write(i+1, j, tmp[j])
        max_count = int(data['COV'].max()) 
        fwp2 = open(samples[i]+'.cov.txt', 'w')
        nx_list = []
        total = float(data.shape[0])
        nxs = []
        for x in range(0,max_count):
            if x % 10 == 0:
                nx = len(data[data['COV']>=x])
                nxs.append([x,nx])
        for i in range(min(50, len(nxs))):
            nx = nxs[i][1]
            x = nxs[i][0]
            fwp2.write('\t'.join(['>='+str(x), str(nx/total)]))
            fwp2.write('\n')
        fwp2.close()
    fwp.save(outfile)
    return {'meanCovStat':outfile}


class MeanCovStatWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(MeanCovStat, params)
 

if __name__ == '__main__':
    covs = sys.argv[1]
    outfile = sys.argv[2]
    samples = sys.argv[3]
    samples = samples.split('-')
    covs = covs.split('-')
    MeanCovStat({'covs':covs, 'samples':samples, 'outfile':outfile})

