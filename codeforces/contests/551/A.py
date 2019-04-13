import sys
n, t = map(int, sys.stdin.readline().split())
before = 200001
index = 0
for i in range(n):
	s, d = map(int, sys.stdin.readline().split())
	if s < t:
		m = (t - s)//d + 1
		s = s + d*m
	if before > s:
		before = s
		index = i+1
print(index)



