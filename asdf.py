A=int(input("낮에 올라간 길이"))
B=int(input("밤에 미끄러진 길이"))
V=int(input("막대기 길이"))

while(x<V):
    D=1
    x=((A*D)-(B*D))

    D+=1

print("%d %d %d->%d" %(A,B,V,D))