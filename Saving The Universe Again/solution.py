def solution(n):
  a=0
  b=1
  for j in range(len(n)):
    if n[j] == 'S':
      a=a+b
    elif n[j] == 'C':
      b=b*2
  return a

N=int(input(''))
for i in range(1,N+1):
  x,y=input().split(" ")
  x=int(x)
  y=list(y)
  z=0
  while x<solution(y):
    k=False
    for j in range(len(y)-1):
      if y[j] == 'C' and y[j+1] == 'S':
        y[j],y[j+1]=y[j+1],y[j]
        z=z+1
        k=True
        if x>=solution(y):
          break
    if k==False:
      z='IMPOSSIBLE'
      break
  print("Case #{}: {}".format(i,z))
