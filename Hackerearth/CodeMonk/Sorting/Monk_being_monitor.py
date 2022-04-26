if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split(' ')))[:N]
        height_dict = dict()
        for i in arr:
            if i in height_dict:
                height_dict[i] += 1
            else:
                height_dict[i] = 1

        max_height = list(height_dict.items())[0][1]
        min_height = max_height

        for k,v in height_dict.items():
            if v > max_height:
                max_height = v
            if v < min_height:
                min_height = v

        if max_height-min_height > 0:
            print(max_height-min_height)
        else:
            print(-1)