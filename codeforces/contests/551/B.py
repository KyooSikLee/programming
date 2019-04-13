import sys

n, m, h = map(int, sys.stdin.readline().split())
x_y = [[0]*m for _ in range(n)]

a_list = list(map(int,sys.stdin.readline().split()))
b_list = list(map(int,sys.stdin.readline().split()))
for i in range(n):
	c_list = list(map(int,sys.stdin.readline().split()))
	for j in range(m):
		if c_list[j] == 1:
			X = a_list[j]
			Y = b_list[i]
			C = int(min(X,Y))
			x_y[i][j] = C

for p in range(n):
	for q in range(m):
		print(x_y[p][q], end=' ')
	print()