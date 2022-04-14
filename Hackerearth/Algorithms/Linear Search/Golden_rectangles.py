if __name__ == '__main__':
	N = int(input())
	count = 0
	for _ in range(N):
		w,h = list(map(int,input().split()))
		if w < h:
			w, h = h, w
		ratio = w/h
		if 1.6 <= ratio <= 1.7:
			count += 1
	print(count)