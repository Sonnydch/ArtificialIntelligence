#print w0
#print w1
#print w2
print "Perceptron Learning:"
samples = [[1,4,-1],[2,9,1],[5,6,1],[4,5,1],[6,0.7,-1],[1,1.5,-1]]
print 'samples are:'
for sam in samples:
    print "x1:",sam[0],"x2:",sam[1],"class:",sam[2]
def prec_learn(_sample,it):
    w0,w1,w2 = 0,0,0
    for i in range(0,it):
        for sam in _sample:
            if(w0+w1*sam[0]+w2*sam[1] >0 and sam[2]==1 or w0+w1*sam[0]+w2*sam[1] <0 and sam[2]==-1):
                pass
            else:
                w0 = w0+1*sam[2]
                w1 = w1+sam[0]*sam[2]
                w2 = w2+sam[1]*sam[2]
        print "after",i+1,"times iteration: w0",w0,"w1",w1,"w2",w2

prec_learn(samples,32)
