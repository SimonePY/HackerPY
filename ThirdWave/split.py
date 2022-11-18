def split_and_join(line):
    Output = line.split();
    Output = "-".join(Output)
    return Output;
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)