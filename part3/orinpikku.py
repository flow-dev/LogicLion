N=int(input())
A = input()
ans=0
for item in A:
  if (item=="j") or (item=="i"):
    ans +=2
  else:
    ans +=1
print(ans)