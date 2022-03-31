# Problem Link
# https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/make-the-cheapest-palindrome-1/

def checkPalindrome(S, mid):
    fS = S[:mid]
    sS = S[-1:-(mid + 1):-1]

    return fS == sS


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        S = input()
        aCost = int(input())
        bCost = int(input())

        Cost_list = {'a': aCost, 'b': bCost}
        mid = int(len(S) / 2)
        length_S = len(S)
        cost = 0
        result_S = ''
        for i in range(len(S)):
            if S[i] == '/':
                v_i = length_S - i - 1
                if S[v_i] != '/':
                    result_S += S[v_i]
                    cost += Cost_list.get(S[v_i])
                else:
                    minCost = sorted(Cost_list.items(), key=lambda x: x[1])[0]
                    result_S += minCost[0]
                    cost += minCost[1]
            else:
                result_S += S[i]

        if checkPalindrome(result_S, mid):
            print(cost)
        else:
            print(-1)
