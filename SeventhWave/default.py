# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split(" "))
locs = defaultdict(set)
[locs[input()].add(loc + 1) for loc in range(n)]
[print(*locs[input()] or {-1}) for _ in range(m)]
