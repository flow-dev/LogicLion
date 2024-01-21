import bisect

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
print(A,B,C,D)

A.sort()
B.sort()
C.sort()
D.sort()
print(A,B,C,D)

Cand = []
for i in range(N):
	Cand.append(A[i])
	Cand.append(B[i])
	Cand.append(C[i])
	Cand.append(D[i])

print(Cand)

Answer = 10000000000

for i in Cand:
	PA = 10000000000
	PB = 10000000000
	PC = 10000000000
	PD = 10000000000
	pos1 = bisect.bisect_left(A, i)
	pos2 = bisect.bisect_left(B, i)
	pos3 = bisect.bisect_left(C, i)
	pos4 = bisect.bisect_left(D, i)
	if pos1 < N: PA = A[pos1]
	if pos2 < N: PB = B[pos2]
	if pos3 < N: PC = C[pos3]
	if pos4 < N: PD = D[pos4]
	Answer = min(Answer, max(PA, PB, PC, PD) - i)

print(Answer)