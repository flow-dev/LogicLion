N=int(input())
S=input()
ans= ""
if (S[N-1] != "G") :
    print(S+"G")
else :
    for i in range (N-1):
        #ans.append(S[i])
        ans += S[i]
    #print("".join(ans))
    print(ans)