# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

dq = deque()

for _ in range(int(input())):
    name, *ele = input().split()
    getattr(dq, name)(*ele)

print(*dq)