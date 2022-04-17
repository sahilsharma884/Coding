if __name__ == "__main__":
    N = int(input())
    A = list(map(int,input().split(' ')))
    M = int(input())
    C = list(map(int,input().split(' ')))

    min_e = C[0] - A[0]
    max_e = C[len(C)-1] - A[len(A)-1]
    B = []
    for e in range(min_e, max_e+1):
        count = 0
        for a in A:
            if a+e in C:
                count += 1

        if count == len(A):
            B.append(e)

    print(*B)