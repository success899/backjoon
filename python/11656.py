import sys
input=sys.stdin.readline

S = str(input().rstrip())
S_list = []

for i in range(len(S)):
    S_list.append(S[i:])

S_list.sort()

for i in S_list:
    print(i)