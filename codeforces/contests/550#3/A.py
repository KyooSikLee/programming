def is_unique(strr):
    """Without using any library functions"""
    def _contains(string, char):
        for c in string:
            if c == char: return True
        return False
    for index in range(len(strr)):
        if _contains(strr[:index], strr[index]): return False
    return True    

num = int(input())
for i in range(num):
	string = input()
	validationList = []
	for j in range(len(string)):
		validationList.append(ord(string[j]))
	validationList.sort()
	if len(string) == 1:
		print("Yes")
		continue
	if validationList[0] + len(string) - 1 != validationList[-1]:
		validation = False
	else:
		validation = True

	if ((is_unique(string) and validation)):
		print("Yes")
	else:
		print("No")
