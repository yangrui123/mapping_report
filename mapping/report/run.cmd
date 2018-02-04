
#### generating mapping report templete --para=1 --mem=2G --docker=

    python /lustre/users/kongdeju/DevWork/jbiot/jbiot/render.py -t /lustre/users/yangrui/devwork/mapping_report/mapping/report/mapping_template.md -j json -o mappingStat.md

#### generating mapping report --para=1 --mem=2G --docker=

    python /lustre/users/kongdeju/DevWork/jbiot/jbiot/md2html.py mappingStat.md
