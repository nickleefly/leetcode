def get_indegrees(nodes):
  counter = {node: 0 for node in nodes}

  for node in nodes:
    for neighbor in node.get_neighbors():
      counter[neighbor] += 1
  return counter

def topological_sort(nodes):
  indegrees = get_indegrees(nodes)
  # all indegree who is 0 put into queue
  queue = collections.deque([
    node
    for node in nodes
    if indegrees[node] == 0
  ])
  # use bfs method to take point from map one by one
  topo_order = []
  while queue:
    node = queue.popleft()
    topo_order.append(node)
    for neighbor in node.get_neighbors():
      indegrees[neighbor] -= 1
      if indegrees[neightbo] == 0
        queue.append(neighbor)
  # check if it depends on loop
  if len(topo_order) != len(nodes):
    return none_loop_depended
  return topo_order
