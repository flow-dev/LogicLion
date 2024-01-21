N = int(input())
S = input()
if S[-1] == 'G':
    print(S[: -1])
    print(S[-1])
else:
    print(S + "G")
    print(S[-1])