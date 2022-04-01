if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        M = []
        for _ in range(N):
            M.append(list(map(int, input().split(' '))))

        i = 0
        count = 0
        while i != N:
            j = 0
            while j != N:
                curr_val = M[i][j]
                for p in range(i, N):
                    for q in range(j, N):
                        if curr_val > M[p][q]:
                            count += 1

                j += 1
            i += 1

        print(count)