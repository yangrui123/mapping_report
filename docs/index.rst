=======
mapping
=======

This is the documentation of **mapping**.

Installation
============
use git to clone code::
    
    git clone git@123.57.226.13:/expan/DevRepos/mapping_report.git


Usage
=====

mapping_report.py -h::

    Usage:
        mapping_report.py -c <parameter>

    Options:
        -h --help
        -c,--conf <parameter>     parameters with yaml format

Here is a sample for yaml file::

    fastqs:
        sample1:
            - ['/home/testData/mapping_report/tumor_R1.fq.gz', 'tumor_R1']
            - ['/home/testData/mapping_report/tumor_R2.fq.gz', 'tumor_R2']
        sample2:
            - ['/home/testData/mapping_report/normal_R1.fq.gz', 'normal_R1']
            - ['/home/testData/mapping_report/normal_R2.fq.gz', 'normal_R2']

    reference         : "hg19.fasta"
    bed               : "bed file"
    mem_of_java       : 10G
    bwa_args          : "args"
    sambamba_sort_args: "args"
    mapping_template  : "mapping_template.md"


Contents
========

.. toctree::
   :maxdepth: 2

   License <license>
   Authors <authors>
   Changelog <changes>
   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
