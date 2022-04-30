def Insertion_sort(A):
    '''
    # Insertion sort. 
    Insertion sort, which is an efficient algorithm for sorting a small number of elements. 
    Insertion sort works the way many people sort a hand of playing cards. We start with an empty left hand 
    and the cards face down on the table. We then remove one card at a time from the table and insert it 
    into the correct position in the left hand. To find the correct position for a card, we compare
    it with each of the cards already in the hand, from right to left.

    The algorithm sorts the input numbers in place: it rearranges the numbers within the array A, with at 
    most a constant number of them stored outside the array at any time.

    T(n) = c1.n + c2.(n-1) + c4.(n-1) + c5.(summation(t[j])) + c6.(summation(t[j]-1)) + c7.(summation(t[j]-1)) + c8.(n-1)

    Best case appear when A is already sorted. So, t[j]=1 as its need to be compare A[i]>key one time. But because of outer for
    loop 'j', summation(t[j]) becomes (1+2+3+....n) = (n-1) times. And summation(t[j]-1) => summation(1-1) = 0, so c6 and c7 cancelled out.

    T(n) = c1.n + c2.(n-1) + c4.(n-1) + c5.(n-1) + c8.(n-1)
    T(n) = (c1 + c2 + c4 + c5 + c8).n - (c2 + c4 + c5 + c8) = a.n + b = O(n)

    Worst case appear when A is sorted in reverse order, in this case, while loop has to compare with key from elements A(j-1 to 0).
    So, t[j] = j for j=1...n

    In c5 term, summation(t[j]) from j=1 to n => summation(j) from j=1 to n => summation(1+2+...n) => [{n.(n+1)}/2] + 1
    In c6 and c7 term, summation(j-1) from j=1 to n => summation(0+1+...n-1) => [{n.(n+1)}/2]

    T(n) = c1.n + c2.(n-1) + c4.(n-1) + c5.([{n.(n+1)}/2] + 1) + c6.[{n.(n+1)}/2] + c7.[{n.(n+1)}/2] + c8.(n-1)
    T(n) = (c5/2 + c6/2 + c7/2).n^2 + (c1 + c2 + c4 + c5/2 + c6/2 + c7/2 + c8).n + (c2 +c4 + c5 + c8)
    T(n) = a.n^2 + b.n + c = O(n^2)

    Best Case = O(n)
    Worst Case = O(n^2)
    
    Parameters:
    A : a sequence of 'n' numbers

    Return:
    Inplace Sorted array
    '''

    for j in range(1, len(A)):  # c1 * n
        key = A[j]  # c2 * (n-1)
        # Insert A[j] into the sorted sequence A[0...j-1]. # 0 * (n-1)
        i = j-1     # c4 * (n-1)
        while i > -1 and A[i] > key:    # c5 * summation(t[j]) from j=1 to n-1 where t[j]
            # is number of times while loop is executed for that value of 'j'
            A[i+1] = A[i]   # c6 * summation(t[j]-1) from j=1 to n-1
            i = i-1 # c7 * summation(t[j]-1) from j=1 to n-1
        A[i+1] = key    # c8 * n-1

    return A

if __name__ == "__main__":
    A = [1,3,4,2,5]
    print(Insertion_sort(A))