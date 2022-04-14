def gcd(X, Y):

    while Y:
        X, Y = Y, X%Y

    return X

if __name__ == "__main__":
    print(gcd(10,11))