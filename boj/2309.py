import sys
import itertools

dwarf_list = []
for i in range(9):
	dwarf_list.append( int(sys.stdin.readline()))

a = list(itertools.combinations(dwarf_list, 7))

for t in a:
	l = list(t)
	if sum(l) == 100:
		l.sort()
		break
for e in l:
	print(e)
