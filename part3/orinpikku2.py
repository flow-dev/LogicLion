X=int(input())
N=int(input())
item=X
ans=0
while item < N:
    r=item%3
    if (r==0):
        item += 1
    elif (r==1):
        item *= 2
    else: #(r==2):
        item *= 3
    ans+=1
print(ans)