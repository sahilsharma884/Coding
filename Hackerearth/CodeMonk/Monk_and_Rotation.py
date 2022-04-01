if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, K = list(map(int, input().split(' ')))
        if K > N:
            K = K % N
        A = list(map(int, input().split(' ')))
        A = A[:N]
        print(' '.join(list(map(str, A[N - K:])) + list(map(str, A[:N - K]))))