# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product


def read_input():
    """Read a line of integers from STDIN."""
    return map(int, input().split())


print(*product(read_input(), read_input()))
