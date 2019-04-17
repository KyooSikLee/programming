import sys
T = int(sys.stdin.readline())
for i in range(T):
	P,M,F,C = map(int, sys.stdin.readline().split())
	chickens = M//P
	coupons = chickens * C
	doo = coupons // F

	sang = coupons // (F-1)
	if coupons % (F-1) == 0:
		sang -= 1
	print(sang, doo)
	print(sang - doo)
