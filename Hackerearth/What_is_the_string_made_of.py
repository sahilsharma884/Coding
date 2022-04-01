# Problem link:
# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/what-is-the-string-made-of-2/

def numDashes(index):
    nD = dict()
    nD['1'] = 2
    nD['2'] = 5
    nD['3'] = 5
    nD['4'] = 4
    nD['5'] = 5
    nD['6'] = 6
    nD['7'] = 3
    nD['8'] = 7
    nD['9'] = 6
    nD['0'] = 6
    return nD.get(index)


if __name__ == '__main__':
    String = input()
    _sum = 0
    for i in String:
        _sum += numDashes(i)
    print(_sum)
