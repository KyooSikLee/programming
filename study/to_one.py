import time
import sys
sys.setrecursionlimit(0x100000)


# Tablulation
cache_tab = [None] * 999999
cache_tab[1] = 0
def to_one_tab(n):
	for i in range(2, n + 1):
		possible_list = []
		possible_list.append(cache_tab[i // 2] + 1) if i % 2 == 0 else None
		possible_list.append(cache_tab[i // 3] + 1) if i % 3 == 0 else None
		possible_list.append(cache_tab[i - 2] + 1) if i - 2 > 0 else None
		cache_tab[i] = min(possible_list)
	return cache_tab[n]

# Memoization
cache_mem = [None] * 999999
cache_mem[1] = 0
def to_one_mem(n):
	if cache_mem[n] != None:
		return cache_mem[n] 
	possible_list = []
	if n % 2 == 0:
		possible_list.append(to_one_mem(n // 2) + 1) 
	if n % 3 == 0:
		possible_list.append(to_one_mem(n // 3) + 1) 
	if n - 2 > 0:
		possible_list.append(to_one_mem(n - 2) + 1)
	cache_mem[n] = min(possible_list)
	return min(possible_list)

# Init timer

tab_start = time.time()
print(to_one_tab(21232))
tab_end = time.time()

print("Tabulation took ",(tab_end - tab_start))

mem_start = time.time()
print(to_one_mem(21232))
mem_end = time.time()

print("Memoization took ",(mem_end - mem_start))




