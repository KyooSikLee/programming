import sys 
N, M, L =  map(int, sys.stdin.readline().split())
station_positions =  list(map(int, sys.stdin.readline().split()))
station_positions.sort()
print(station_positions)