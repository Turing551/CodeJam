def solution(k):
    ans=''
    for i in k:
        ans+='E' if i=='S' else 'S'
    return ans
n=int(input())  
for j in range(1,n+1):
    x=int(input())
    y=input()
    print("Case #{}: {}".format(j,solution(y)))
