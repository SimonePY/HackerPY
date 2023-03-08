# Enter your code here. Read input from STDIN. Print output to STDOUT
n, s = int(input()), set(map(int, input().split()[::-1]))
for _ in range(int(input())):
    method, *args = input().split()
    getattr(s, method)(*map(int, *args)) if args else getattr(s, method)()
print(sum(s))