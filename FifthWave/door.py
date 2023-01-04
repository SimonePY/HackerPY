# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
design = '.|.'
dash = '-'

for i in range(1, n, 2):
    print((design * i).center(m, dash))
print('WELCOME'.center(m, dash))

for i in range(n - 2, 0, -2):
    print((design * i).center(m, dash))
