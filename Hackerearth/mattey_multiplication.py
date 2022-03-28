# Problem link:
# https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/mattey-multiplication-6/

def pfByN(op1, op2):
    multi = op1 * op2
    list_op = []

    while multi:
        pow_i = 1
        while multi >= op1 << pow_i:
            pow_i += 1
        pow_i -= 1
        multi -= op1 << pow_i
        list_op.append(pow_i)

    return list_op


if __name__ == '__main__':
    N = 5
    M = 21
    result = ''
    list_op = pfByN(N, M)
    for op1 in range(len(list_op)):
        result += f'({N}<<{list_op[op1]})'
        if len(list_op) != op1 + 1:
            result += ' + '
    print(result)
