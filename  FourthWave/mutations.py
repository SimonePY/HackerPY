def mutate_string(string, position, character):
    out = [i for i in string]
    out[position] = character
    return "".join(i for i in out)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
