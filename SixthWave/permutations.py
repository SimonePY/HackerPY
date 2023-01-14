# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

str, i = input().split()
p = sorted(list(permutations(str, int(i))))
for i in p:
    print(''.join(i))
