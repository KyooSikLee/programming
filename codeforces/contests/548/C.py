nk = input().split(" ")
n = int(nk[0])
k = int(nk[1])
redList = [False]*n

iter = 0
cache = {}
for i in range(n-1):
    appended = False
    l = input().split(" ")
    l0 = int(l[0])
    l1 = int(l[1])
    l2 = int(l[2])
    if l2 == 0:
        if redList[l0] == True and redList[l1] == True:
            pass
        elif redList[l0] == True:
            
        elif redList[l1] == True:
            
        else:
            cache[iter] = [l0, l1]
            iter += 1

minus = 0
for c in cache:
    p = (len(cache[c]))
    minus += ((p**k)- p)
print((n**k-n-minus) % (10**9 + 7))

# 13 3
# 9 13 1
# 8 3 1
# 11 9 0
# 8 13 0
# 10 9 0
# 2 7 0
# 4 8 1
# 11 5 0
# 10 12 0
# 12 1 1
# 5 7 0
# 6 8 1