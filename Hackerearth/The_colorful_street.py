# Problem Link:
# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/the-colorful-street-1/?utm_source=header&utm_medium=search&utm_campaign=he-search

def minCost(paints):
    h2 = paints[0]
    for i in range(1, len(paints)):
        h1, h2 = paints[i - 1], paints[i]
        h2[0] += min(h1[1], h1[2])
        h2[1] += min(h1[0], h1[2])
        h2[2] += min(h1[0], h1[1])

    print(min(h2))


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N_Houses = int(input())
        paints = []
        for _ in range(N_Houses):
            paints.append(list(map(int, input().split(' '))))

        minCost(paints)
