def change(list):
	print(list)
	if list[0] == 12:
		return list
	list[0]+=1
	return change(list)

print(change([1,2]))