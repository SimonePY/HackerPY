def merge_the_tools(string, k):
    l = len(string) // k
    for i in range(l):
        print(''.join(dict.fromkeys(string[i * k:(i * k) + k])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
