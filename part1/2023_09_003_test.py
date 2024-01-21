N = int(input())

S = input()
T = input()

count = 0
for s,t in zip(S,T):
    if s != t:
        count += 1
        
print(count)

# from scipy.spatial import distance

# N=int(input())
# S=input()
# T=input()

# print(int(distance.hamming(list(S), list(T))*N))