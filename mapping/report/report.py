from config import render
import config
from jbiot import log
import os
from config import md2html

cwd = os.path.dirname(os.path.abspath(__file__))
mappingTemplt = os.path.join(cwd, 'mapping_template.md')
#render = os.path.join(cwd,'render.py')


def report(ijson):
    out = "mappingStat.md"
    cmd = "python %s -t %s -j %s -o %s" %(render, mappingTemplt, ijson, out)
    log.run("generating mapping report templete", cmd)
    cmd = "python %s %s" %(md2html, out)
    log.run("generating mapping report", cmd)

