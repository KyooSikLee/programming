def Cluster(adjList, visited):

nk =  input().split(" ")
n = int(nk[0])
k = int(nk[1])

adjList = [[] for i in range(n+1)]
visited = [False]*(n+1)
lookupList = []
iteration = 0
for i in range(n-1):
    l = input().split(" ")
    l0 = int(l[0])
    l1 = int(l[1])
    l2 = int(l[2])
    if l2 == 0:
        adjList[l0].append(l1)
        adjList[l1].append(l0)
        lookupList.append(l0)
        lookupList.append(l1)

lookupList = (list(set(lookupList)))

print(visited)
print(lookupList)
print(adjList)
# print((n**k-n-minus) % (10**9 + 7))

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
