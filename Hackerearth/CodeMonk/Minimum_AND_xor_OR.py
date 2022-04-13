def compute_min_XOR(arr, i, j):
    return (arr[i] & arr[j]) ^ (arr[i] | arr[j])

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split(' ')))[:N]

        min_val = compute_min_XOR(A,0,1)
        for i in range(N):
            for j in range(N):
                if i!=j:
                    if min_val > compute_min_XOR(A,i,j):
                        min_val = compute_min_XOR(A,i,j)
        
        print(min_val)
