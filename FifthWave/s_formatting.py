def print_formatted(number):
    # your code goes here
    width = len(str(bin(number)[2:]))
    for num in range(1, number + 1):
        d = str(num)
        o = str(oct(num))[2:]
        h = str(hex(num))[2:].upper()
        b = str(bin(num))[2:]
        print(f"{d.rjust(width)} {o.rjust(width)} {h.rjust(width)} {b.rjust(width)}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
