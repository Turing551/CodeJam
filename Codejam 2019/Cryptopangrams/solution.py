def solve(p,q):
    while q>0:
        r=p%q
        p=q
        q=r
    return p
def solution(ctxt):
    a=len(ctxt)
    txt=(a+1)*[0]
    for i in range(a-1):
        if ctxt[i] != ctxt[i+1]:
            temp=i+1
            txt[temp]=solve(ctxt[i],ctxt[i+1])
    for i in range(temp-1,-1,-1):
        txt[i]=ctxt[i]/txt[i+1]
    for i in range(temp,a):
        txt[i+1]=ctxt[i]/txt[i]
    res=list(set(txt))
    res.sort()
    arr={y: chr(x+ord('A')) for x,y in enumerate(res)}
    return ''.join([arr[no] for no in txt])

n=int(input())
for i in range(1,n+1):
    [a,b]=[int(z) for z in input().split(" ")]
    ctxt=[int(z) for z in input().split(" ")]
    print("Case #{}: {}".format(i,solution(ctxt)))
