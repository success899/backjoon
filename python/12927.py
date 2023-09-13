import sys
input=sys.stdin.readline

switch = [0] + list(input().rstrip())
count = 0

for i in range(1, len(switch)):
    if switch == [0] + ['N'] * (len(switch)-1):
        break

    if switch[i] == 'N':
        continue

    for j in range(i, len(switch)):
        if j % i == 0:
            if switch[j] == 'Y':
                switch[j] = 'N'
            else:
                switch[j] = 'Y'
    count += 1 
    
print(count)