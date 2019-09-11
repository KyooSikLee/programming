import sys
class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distance[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, paths



N, M = map(int, sys.stdin.readline().split())
while( N + M ):
  graph = Graph()
  # initialization
  for i in range(N+1):
  	graph.add_node(i)

  for i in range(M):
    line = sys.stdin.readline().split()
    if line[0] == '!':
      a, b, w = map(int, line.split()[1:3])
      graph.add_edge(a, b, w)

    elif line[0] == '?':
      a, b = map(int, line.split()[1:2])
      print(dijsktra(graph, a))




















