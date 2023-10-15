N = int(input())
A = list(map(int, input().split()))

print(N)
print(A)

pushed = [False] * 10

for i in range(N):
    pushed[A[i]] = True
    #print(pushed,A[i])

for i in range(10):
    if pushed[i]:
        print(i)
