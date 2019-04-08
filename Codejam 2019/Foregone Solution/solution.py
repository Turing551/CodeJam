n=int(input())
for i in range(1,n+1):
    temp=input()
    list=[int(k) for k in temp]
    x=0
    y=int(temp)
    for j,k in enumerate(list[::-1]):
        if k==4:
            res=(10**j)*2
            x=x+res
            y=y-res
    print("Case #{}: {} {}".format(i,y,x))
