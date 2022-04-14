if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        N, k = list(map(int, input().split(' ')))
        A = input()
        
        p = -1
        max_ = ''
        B = A
        for i in range(N):
            if max_ < A:
                max_ = A
                offset = i
            elif B == A:
                p = i
                break
            
            A = A[1:] + A[:1]
        if p == -1:
            print(offset+N*(k-1))
        else:
            print(offset+p*(k-1))