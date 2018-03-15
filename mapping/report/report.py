#! /usr/bin/env python 
try:
    from config import render
    from config import md2html
except:
    render = 'render.py'
    md2html = 'md2html.py'
from jbiot import log
from jbiot import jbiotWorker
import os


def get_templt(remotefile):
    home = os.environ["HOME"]
    localfile = remotefile.split("/")[-1]
    cmd = "wget %s -P %s/.templates " % (home,remotefile)

    localfile1 = os.path.join(home,".templates",localfile)
    localfile2 = os.path.join("~",".templates",localfile)
    if os.path.exists(localfile1):
        return localfile1
    os.system(cmd)
    return localfile1



def report(parms):
    '''Generating report

    Args:
        parms (dict) : which has the following keys::
        
            {
                template  : template of report
                templtJson: json file, input parameter for template
            }
    
    Returns:
        dict : ``{"outfile":"report"}``
    '''
    mappingTemplt = parms['template']
    if mappingTemplt.startswith("http://"):
        mappingTemplt = get_templt(mappingTemplt)
    ijson = parms['templtJson']
    out = "mapping_report.md"
    cmd = "%s -t %s -j %s -o %s" %(render, mappingTemplt, ijson, out)
    log.run("generating mapping report templete", cmd)
    cmd = "%s %s" %(md2html, out)
    log.run("generating mapping report", cmd)
    return {'outfile': out}


class ReportWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(report, params)
