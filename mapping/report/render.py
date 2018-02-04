from jinja2 import Template
import json
import os
import sys
import xlrd
import base64
reload(sys)
sys.setdefaultencoding('utf-8')

dirpath = os.path.dirname(os.path.abspath(__file__))
macro = os.path.join(dirpath,"func.macro")

def render(tpl,ijson,out):
    fwp = open(out,'w') 
    fcont = open(tpl).read()
    im = open(macro,'r').read()
    fcont = im + fcont
    fwp.write(fcont)
    fwp.close()
    temp = Template(fcont)
    temp.globals['open'] = open
    temp.globals['base64'] = base64.b64encode
    idict = json.loads(open(ijson).read())
    cov = idict["targetRegionCovStat"]
    cov_data = xlrd.open_workbook(cov)
    cov_table = cov_data.sheets()[0]
    idict["targetRegionCovStat"] = cov_table
    rate = idict["mappingRateStat"]
    rate_data = xlrd.open_workbook(rate)
    rate_table = rate_data.sheets()[0]
    idict["mappingRateStat"] = rate_table
    args = idict
    tmd = temp.render(**args)
    
    fp = open(out,"w")
    fp.write(tmd)
    fp.close()

    return tmd 



if __name__ == "__main__":
    import sys
    from docopt import docopt

    usage = """
    Usage:
        render.py -t <template> -j <ijson> -o <output>

    Options:
        -t <template> --template=<template>      tempate to render
        -j <json> --json=<ijson>                 args json dict
        -o <out> --out=<out>                     output
        
    """
    args = docopt(usage)    
    tp = args["--template"]
    ij = args["--json"]
    ot = args["--out"]
    render(tp,ij,ot)


