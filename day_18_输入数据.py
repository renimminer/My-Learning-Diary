temp=True
count=0
while (temp and count<5):
    (x,y)=(int(x) for x in input().split())
    ary1=input().split()
    ary2=input().split()
    ary1.extend(ary2)
    ary3=[]
    ary3=[int(i) for i in ary1]
    ary4=[]
    ary4=list(set(ary3))
    ary4.sort()
    ary5=[]
    ary5=[str(i) for i in ary4]
    print (' '.join(ary5))
    count=count+1