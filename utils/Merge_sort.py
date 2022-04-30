def Merge(A,p,q,r):
    '''
    The merge sort algorithm closely follows the divide-and-conquer paradigm. Intuitively, it operates as follows.
    Divide: Divide the n-element sequence to be sorted into two subsequences of n/2 elements each.
    Conquer: Sort the two subsequences recursively using merge sort.
    Combine: Merge the two sorted subsequences to produce the sorted answer.

    The key operation of the merge sort algorithm is the merging of two sorted sequences in the “combine” step. We merge by calling 
    an auxiliary procedure MERGE(A, p, q, r), where A is an array and p, q, and r are indices into the array such that p <= q < r.

    The procedure assumes that the subarrays A[p...q] and A[q+1...r] are in sorted order. 
    It merges them to form a single sorted subarray that replaces the current subarray A[p...r]

    T(n) = c1.n + c2.(n-1) + c3.(n-1) + c4.(n-1) + c5.(n-1) + c6.(n-1) + c7.(n-1)
    T(n) = (c1 + c2 + c3 + c4 + c5 + c6 + c7).n - (c2 + c3 + c4 + c5 + c6 + c7)
    T(n) = a.n - b = O(n)

    Space Complexity = L and R variable taken additional array = O(n1 + n2)

    Parameters:
    A : a sequence of array
    p : start index
    q : middle index
    r : end index
    where A[p...q] & A[q+1...r] are in sorted array

    Return
    Merge with sorted array from two sorted sub-arrays
    '''
    n1 = q - p + 1  # constant time
    n2 = r - q  # constant time
    
    L = A[p:q+1]    # n1 times
    R = A[q+1:r+1]  # n2 times

    import math
    L.append(math.inf)  # constant time
    R.append(math.inf)  # constant time

    i,j = 0,0   # constant time

    for k in range(p,r+1):  # n1+n2 = c1.n times
        if L[i] <= R[j]:    # c2.(n-1)
            A[k] = L[i]     # c3.(n-1)
            i += 1          # c4.(n-1)
        else:   # c5.(n-1)
            A[k] = R[j]     # c6.(n-1)
            j += 1          # c7.(n-1)

def Merge_sort(A,p,r):
    '''
    If p >= r , the subarray has at most one element and is therefore already sorted. 
    Otherwise, the divide step simply computes an index q that partitions A[p...r] into two subarrays: 
    A[p...q], containing n/2 elements, and A[q+1...r], containing n/2 elements.

    T(n) = 2T(n/2) + o(n)
    # Solving with master theorem or recurrence tree : O(nlg(n))
    T(n) = 2T(n/2) + c.n
    2T(n/2) = 2[ 2T(n/4) + c.n/2 ] = 4T(n/4) + c.n
    4T(n/4) = 4[ 2T(n/8) + c.n/4 ] = 8T(n/8) + c.n and so on
    
    So, for every subproblems, each level takes c.n times. Since, the problems are dividing into sub-problems,
    level of the tree will be lg(n).
    T(n) = cn.log(n) = O(nlg(n))
    '''
    if p < r:
        # Divide: The divide step just computes the middle of the subarray, which takes constant time. O(1) 
        q = (p+r)//2
        # Conquer: We recursively solve two subproblems, each of size n/2, which contributes 2T(n/2) to running time
        Merge_sort(A,p,q)
        Merge_sort(A,q+1,r)
        # Combine: Noted Merge() that takes O(n)
        Merge(A,p,q,r)


if __name__ == "__main__":
    A = [5,2,4,7,1,3,2,6]
    Merge_sort(A,0,len(A)-1)
    print(A)
    