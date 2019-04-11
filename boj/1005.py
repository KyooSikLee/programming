T = int(input())
for i in range(T):
	cache = {}
	NK = list(map(int,input().split()))
	N = NK[0]
	K = NK[1]
	D = list(map(int,input().split()))
	for j in range(K):
		XY = input().split(" ")
		X = int(XY[0])
		Y = int(XY[1])
		if X in cache.keys():
			cache[X].append(Y)
		else:
			cache[X] = [Y]
	W = int(input())
	