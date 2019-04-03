def solve(n):
  a='OK';
  for j in range(len(n)-1):
    if n[j]>n[j+1]:
      a=j
      break;
  return a

N=int(input(''))
arr=[]
for i in range(N):
  arr.append([int(input('')), input('')])
  arr[i][1]=[int(s) for s in arr[i][1].split(" ")]

for i in range(len(arr)):
  k=False
  while not k:
    k=True
    for j in range(arr[i][0]-2):
      if arr[i][1][j]>arr[i][1][j+2]:
        k=False
        arr[i][1][j],arr[i][1][j+2]=arr[i][1][j+2],arr[i][1][j] 
  print("Case #{}: {}".format(i+1,solve(arr[i][1])))
