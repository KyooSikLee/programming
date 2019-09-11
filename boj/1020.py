import sys 
number = list(map(int, list(sys.stdin.readline())))
length = len(number)
############[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
line_list = [6, 2, 5, 5, 4, 5, 6, 3, 7, 5]

dp = [[None]*106]*16
dp[1][2] = 1
dp[1][3] = 7
dp[1][4] = 4
dp[1][5] = 2
dp[1][6] = 0
dp[1][7] = 8
for i in range(2, 16):
	for j in range(i * 2, (i * 7) + 1):
		dp[i][j] = dp[i-1]



