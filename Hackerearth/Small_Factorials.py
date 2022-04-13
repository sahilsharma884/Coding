# Problem Link:
# https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/small-factorials/

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        prod = 1
        while N > 0:
            prod *= N
            N -= 1

        print(prod)