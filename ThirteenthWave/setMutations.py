len_A = int(input())
A = set([int(x) for x in input().split()])
num_of_other_sets = int(input())

for _ in range(num_of_other_sets):
    op_name, _ = input().split()
    other_set = set([int(x) for x in input().split()])
    set_op = getattr(A, op_name)

    set_op(other_set)

print(sum(A))
