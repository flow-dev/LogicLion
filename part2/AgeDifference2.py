N=int(input())
A = list(map(int, input().split()))
old=max(A)
yong=min(A)
for i in range(N):
  print(old-yong)