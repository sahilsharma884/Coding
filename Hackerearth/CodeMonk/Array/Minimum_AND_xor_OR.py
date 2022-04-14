def compute_min_XOR(arr, i, j):
    # return (arr[i] & arr[j]) ^ (arr[i] | arr[j])
    return arr[i] ^ arr[j] # reduced form

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split(' ')))[:N]

        
        # O(n^2)
        # min_val = compute_min_XOR(A,0,1)
        # for i in range(N):
        #     for j in range(N):
        #         if i!=j:
        #             if min_val > compute_min_XOR(A,i,j):
        #                 min_val = compute_min_XOR(A,i,j)

        # After learning the approach from others
        # Sort the array and perform XOR between adjacent
        # O(nlogn)
        A = sorted(A, reverse=True) 
        min_val = compute_min_XOR(A,0,1)
        for i in range(1,N-1):
            if min_val > compute_min_XOR(A,i,i+1):
                min_val = compute_min_XOR(A,i,i+1)
        
        print(min_val)