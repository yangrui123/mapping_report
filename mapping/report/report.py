try:
    from config import render
    from config import md2html
except:
    render = 'render.py'
    md2html = 'md2html.py'
import config
from jbiot import log
from jbiot import jbiotWorker
import os

cwd = os.path.dirname(os.path.abspath(__file__))
mappingTemplt = os.path.join(cwd, 'mapping_template.md')



def report(parms):
    mappingTemplt = parms['template']
    ijson = parms['templtJson']
    out = "mapping_report.md"
    cmd = "%s -t %s -j %s -o %s" %(render, mappingTemplt, ijson, out)
    log.run("generating mapping report templete", cmd)
    cmd = "python %s %s" %(md2html, out)
    log.run("generating mapping report", cmd)
    return {'outfile': out}


class ReportWorker(jbiotWorker):
    def handle_task(self, key, params):
        self.execute(report, params)
