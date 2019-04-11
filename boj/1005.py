cache = {}
def calculate(adj, D, W):
	if W in cache.keys():
		return cache[W]
	if W not in adj.keys():
		cache[W] = D[W-1]
		return D[W-1]
	else:
		cache[W] = D[W-1] + max(map(lambda x: calculate(adj, D, x), adj[W]))
	return cache[W]

T = int(input())
for i in range(T):
	adj = {}
	N, K = list(map(int,input().split()))
	D = list(map(int,input().split()))
	for j in range(K):
		X, Y = list(map(int,input().split()))
		if Y in adj.keys():
			adj[Y].append(X)
		else:
			adj[Y] = [X]
	W = int(input())
	cache = {1: D[0]}
	print(calculate(adj, D, W))