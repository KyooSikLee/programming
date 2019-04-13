import sys
cache = []
def calculate(s, length, next_index, open_count):
	if next_index == length and open_count == 1:
		cache.append(s)
		return
	else:
		return
	if open_count > length//2:
		return
	
	if s[next_index] == '(':
		calculate(s, length, next_index + 1, open_count + 1)
		return
	elif s[next_index] == ')':
		calculate(s, length, next_index + 1, open_count - 1)
		return
	else:
		calculate(s, length, next_index + 1, open_count + 1), 
		calculate(s, length, next_index + 1, open_count - 1)


length = int(sys.stdin.readline())
s = ['!'] + list(sys.stdin.readline())

if (length % 2 == 1) or s[1] == ')' or s[length] == '(':
	print(":(")
	sys.exit()

calculate(s, length, 2, 1)
print(cache)