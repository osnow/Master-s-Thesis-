args = commandArgs(trailingOnly=TRUE)
sim1<-read.table(file=args[1])
sim2<-read.table(file=args[2])
rownames(sim1)<-sim1$V1
rownames(sim2)<-sim2$V1
dt<-merge(sim1, sim2, by=0, all=TRUE)[c(1,3,5)]
dt[is.na(dt)] <- 0
write.table(dt,row.names=FALSE,col.names=FALSE,file="merged.txt")