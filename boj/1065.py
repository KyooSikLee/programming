import sys
def is_sequence(T):
	length = len(T)
	if len(T) < 3:
		return True

	distance = T[1] - T[0]
	for i in range(1, length):
		if T[i] - T[i - 1] != distance:
		 	return False
	return True


T = int(sys.stdin.readline())

result = 0
for i in range(1, T + 1):
	string = str(i)
	string = list(map(lambda c: int(c), string))
	if is_sequence(string):
		result += 1

print(result)