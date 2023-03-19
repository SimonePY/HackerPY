# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

N, M = map(int, input().split())
lists = []
for _ in range(N):
    lists.append(map(int, input().split()[1:]))

print(max([sum(map(lambda x: x * x, a)) % M for a in product(*lists)]))
