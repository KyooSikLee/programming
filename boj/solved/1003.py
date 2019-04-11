cache = {}
cache[0] = [1,0]
cache[1] = [0,1]
for i in range(2, 41):
  zeros = cache[i-1][0] + cache[i-2][0]
  ones = cache[i-1][1] + cache[i-2][1]
  cache[i] = [zeros, ones]
T = int(input())
for i in range(T):
  N = int(input())
  print("%d %d" %( cache[N][0], cache[N][1]))
