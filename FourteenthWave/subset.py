# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        n1 = int(input())
        a = set(map(int, input().split()))
        n2 = int(input())
        b = set(map(int, input().split()))
        if a == a.intersection(b):
            print(True)
        else:
            print(False)
