mod = 1000000009
store1 = {}

def ans(n):
    if n < 25000:
        if n in store1.keys():
            return store1[n]

        if n == 0:
            store1[n] = 1
            return store1[n]
        if n == 1:
            store1[n] = 10
            return store1[n]

        x = ans(n//2)
        y = ans(n//2-1)

        if not n & 1:    
            store1[n] = ((x*x) - (y*y)) % mod
        else:
            z = ans(n//2+1)
            store1[n] = (x * (z - y)) % mod

        return store1[n]

    else:
        if n in store2.keys():
            return store2[n]

        if n == 0:
            store2[n] = 1
            return store2[n]
        if n == 1:
            store2[n] = 10
            return store2[n]

        x = ans(n//2)
        y = ans(n//2-1)

        if not n & 1:    
            store2[n] = ((x*x) - (y*y)) % mod
        else:
            z = ans(n//2+1)
            store2[n] = (x * (z - y)) % mod

        return store2[n]


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        store2 = {}
        N = int(input())
        print(ans(N))