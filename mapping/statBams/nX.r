#!/usr/bin/env Rscript
library(ggplot2)
library(Cairo)
args  = commandArgs(T)
filename = args[1]
prefix = args[2]
title = args[3]
data = read.table(filename, sep='\t', header=F)
data[,1] = factor(data[,1],factor(data[,1]))
Cairo(file=paste(prefix,".region.coverage.png",sep=""),type="png",units="in",bg="white",width=12, height=6, pointsize=12, dpi=300)
base = ggplot(data,aes(data[,1],data[,2]))+geom_bar(stat="identity",fill="#1890f0",width=0.3)+labs(x="Coverage",y="Target region precent(%)", title=title)
ghline = geom_hline(yintercept = 0,lty=1,col="grey",lwd=1)
text = theme(axis.text.x = element_text(face="bold", color="black", size=8,angle=60,hjust=0.5),panel.background=element_blank(),axis.ticks = element_blank())
len = dim(data)[1]
base+ghline+text+theme(plot.title=element_text(hjust=0.5))
dev.off()

Cairo(file=paste(prefix,".region.coverage.pdf",sep=""),type="pdf",units="in",bg="white",width=120, height=60, dpi=300)
text = theme(axis.text.x = element_text(face="bold", color="black", size=16,angle=60,hjust=0.5),axis.text.y = element_text(face="bold", color="black", size=16),panel.background=element_blank(),axis.ticks = element_blank(),text=element_text(size=16))
base+ghline+text+theme(plot.title=element_text(hjust=0.5))
dev.off()
