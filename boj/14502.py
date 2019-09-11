import sys
import copy
from itertools import combinations 


def find_all_indices(cells, value):
	indices = []
	for i in range(len(cells)):
		if cells[i] == value:
			indices.append(i)
	return indices


def count(cells, value):
	val = 0
	for i in range(len(cells)):
		if cells[i] == value:
			val += 1
	return val


def min_num_safe(n, m, cells):
	zero_list = find_all_indices(cells, 0)

	combinations_list = combinations(zero_list, 3)

	value_list = []
	for comb in combinations_list:
		new_cells = copy.copy(cells)
		for index in comb:
			new_cells[index] = 1

		infect(n, m, new_cells)
		value_list.append(count(new_cells, 0))


	return max(value_list)

def index_of(cells, value):
	for i in range(len(cells)):
		if cells[i] == value:
			return i
	return None



def infect(n, m, cells):
	index = index_of(cells, 2)
	if index == None:
		return
	cells[index] = 3

	if index + m < maximum and (cells[index + m] == 0 or cells[index + m] == 2):
		cells[index + m] = 2
		infect(n, m, cells)

	if index - m > minimum and (cells[index - m] == 0 or cells[index - m] == 2):
		cells[index - m] = 2
		infect(n, m, cells)

	if index % m != 0 and (cells[index - 1] == 0 or cells[index - 1] == 2):
		cells[index - 1] = 2
		infect(n, m, cells)

	if index % m != (m - 1) and (cells[index + 1] == 0 or cells[index + 1] == 2):
		cells[index + 1] = 2
		infect(n, m, cells)

	infect(n, m, cells)
	return

def nice_print(n, m, cells):
	for i in range(n):
		for j in range(m):
			print(cells[i*m + j], end=' ')
		print()




N, M = map(int, sys.stdin.readline().split())
maximum = N * M
minimum = 0
cell_list = []
for i in range(N):
	for j in map(int, sys.stdin.readline().split()):
		cell_list.append(j)

print(min_num_safe(N, M, cell_list))