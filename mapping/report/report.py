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
    ijson = parms['templtJson']
    out = "mapping_report.md"
    cmd = "%s -t %s -j %s -o %s" %(render, mappingTemplt, ijson, out)
    log.run("generating mapping report templete", cmd)
    cmd = "%s %s" %(md2html, out)
    log.run("generating mapping report", cmd)
    return {'outfile': out}


class ReportWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(report, params)
