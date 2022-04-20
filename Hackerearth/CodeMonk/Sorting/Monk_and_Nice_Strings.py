if __name__ == "__main__":
    N = int(input())
    st = [input()]
    print(0)
    for i in range(1,N):
        count = 0
        com = input()
        for j in range(len(st)):
            if com > st[j]:
                count += 1
        
        print(count)
        st.append(com)
