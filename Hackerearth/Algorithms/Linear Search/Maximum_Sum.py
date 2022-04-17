if __name__ == '__main__':
    N = int(input()) # Store Number of size of an elements
    A = list(map(int, input().split(' '))) # Take input as integer type
    flag = 0 # To indicate whether there is any positive present it or not
    for i in A: # iterating to find if any positive number present in it
        if i >= 0:
            flag = 1
            break

    if flag == 0: # if all are negative numbers
        sum_ = A[0]
        count = 1
        for i in A:
            if sum_ < i:
                sum_ = i

    else:
        sum_ = 0
        count = 0
        for i in A:
            if i > -1:
                sum_ += i
                count += 1

    print(sum_, count)