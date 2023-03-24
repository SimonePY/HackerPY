# Enter your code here. Read input from STDIN. Print output to STDOUT
main_set = set(map(int, input().split()))
b = int(input())
lst = []
for i in range(b):
    s2 = set(map(int, input().split()))
    lst.append(main_set.issuperset(s2))
if False in lst:
    print(False)
else:
    print(True)
