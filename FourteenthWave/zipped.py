# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())

array = []
for i in range(x):
    array.append(list(map(float, input().split())))

for j in zip(*array):
    print(sum(j) / len(j))
