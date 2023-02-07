# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

a, b = list(map(str, input().split()))
for i in range(1, int(b) + 1):
    for d in list(combinations(sorted(str(a)), i)):
        print("".join(d))
