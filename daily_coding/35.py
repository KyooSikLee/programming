def swap(some_list, i, j):
	temp = some_list[i]
	some_list[i] = some_list[j]
	some_list[j] = temp
	return

arr = ['G', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'B', 'R', 'G']

Rcount = 0
Gcount = 0
length = len(arr)
for i in range(length):
	if arr[i] == 'R':
		swap(arr, i, Rcount)
		Rcount += 1
for i in range(Rcount + 1 ,length):
	if arr[i] == 'G':
		swap(arr, i, Rcount + Gcount)
		Gcount += 1
print(arr)

