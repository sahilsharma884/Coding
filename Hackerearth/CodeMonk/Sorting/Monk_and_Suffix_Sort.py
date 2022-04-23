if __name__ == "__main__":
    S, k = input().split(' ')
    k = int(k)

    suf = list()
    occ_letter = dict()

    for i in range(len(S)):
        suf.append(S[i:])

    suf.sort()
    
    for i in range(len(S)):
        if S[i] in occ_letter:
            occ_letter[S[i]] += 1
        else:
            occ_letter[S[i]] = 1

    for ky,v in occ_letter.items():
        if v-k < 0:
            k = k-v
        else:
            occ_chosen_char = k
            break
    
    chosen_char = ky

    for i in range(len(S)):
        if chosen_char == S[i]:
            occ_chosen_char -= 1

        if occ_chosen_char == 0:
            break

    print(suf[i])