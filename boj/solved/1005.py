import sys 
sys.setrecursionlimit(100000)
cache = [None]*1001
def calculate(adj, D, W):
	if cache[W] != None: 
		return cache[W]
	if adj[W] == None:
		cache[W] = D[W]
	else: ## cache[W] == None
		cache[W] = D[W] + max(map(lambda x: calculate(adj, D, x), adj[W]))
	return cache[W]

T = int(sys.stdin.readline())
for i in range(T):
	N, K = map(int,sys.stdin.readline().split())
	D = [0] + list(map(int,sys.stdin.readline().split()))
	adj = [None] * (N+1)
	for i in range(K):
		X, Y = map(int, sys.stdin.readline().split())
		if adj[Y] == None:
			adj[Y] = [X]
		else:
			adj[Y].append(X)

	W = int(sys.stdin.readline())
	cache = [None]*(N+1)
	print(calculate(adj, D, W))