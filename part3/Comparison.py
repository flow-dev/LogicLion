N=map(int(input()))
M=map(int(input()))
A=[]
B=[]
for i in range(N):
  for j in range(M):
    if A[i]<B[j] or A[i]==B[j] :
      print()