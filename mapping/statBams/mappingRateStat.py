import sys, os
import config
from jbiot import log
import xlwt
import json


def mappingRateStat(targetFile, tstats, dstats, bstats, samples):
    fwp = xlwt.Workbook()
    sheet1 = fwp.add_sheet('sheet1', cell_overwrite_ok=True)
    head = ['Sample', 'Total mapping rate', 'Proper rate', 'Deduplicated rate', 'Targeted rate']
    for i in range(len(head)):
        sheet1.write(0,i,head[i])
    for i in range(len(tstats)):
        fp = open(tstats[i])
        lines = fp.readlines(); fp.close()
        for line in lines:
            if 'mapped' in line and '%' in line:
                total_mapped = float(line.split()[0])
                total_rate = line.split('(')[-1].split(':')[0]
            elif 'properly' in line:
                proper_rate = line.split('(')[-1].split(':')[0]
        fp2 = open(dstats[i], 'r')
        lines1 = fp2.readlines();fp2.close()
        for line in lines1:
            if 'mapped' in line and '%' in line:
                dedup = float(line.split()[0])
                dedup_rate = "%.2f%%"%((1-dedup/total_mapped)*100)
                break
        fp3 = open(bstats[i],'r')
        lines2 = fp3.readlines();fp3.close()
        for line in lines2:
            if 'mapped' in line and '%' in line:
                target = float(line.split()[0])
                target_rate = "%.2f%%"%((target/dedup)*100)
                break
        tmp = [samples[i], total_rate, proper_rate, dedup_rate, target_rate]
        for j in range(len(tmp)):
            sheet1.write(i+1, j, tmp[j])
    fwp.save(targetFile)
        

if __name__ == '__main__':
    targetFile = sys.argv[1]
    sstats = sys.argv[2]
    dstats = sys.argv[3]
    tstats = sys.argv[4]
    samples = sys.argv[5]
    sstats = sstats.split('-')
    dstats = dstats.split('-')
    tstats = tstats.split('-')
    samples = samples.split('-')
    rate = mappingRateStat(targetFile, sstats, dstats, tstats, samples)

