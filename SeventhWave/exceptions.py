for __ in range(int(input())):
    a, b = input().split()
    try:
        a, b = int(a), int(b)
        quotient: int = a // b
    except (ValueError, ZeroDivisionError) as e:
        print("Error Code:", e)
    else:
        print(quotient)