import sys
T = int(sys.stdin.readline())
for i in range(T):
	N,W = map(int, sys.stdin.readline().split())
	inner = map(int, sys.stdin.readline().split())
	outer = map(int, sys.stdin.readline().split())
print(N,W,inner,outer)