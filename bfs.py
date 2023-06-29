def bfs(start_node):
  # use queue, dont use stack
  # distance(dict) has two purpose, one is to record a point if its been put into
  # a queue, to avoid duplicated visit, another is to record the distance
  # start_node to other node. If only checking connectivity, we can use set
  # node as key is to compare memory address
  queue = collections.deque([start_node])
  distance = {start_node: 0}

  # while queue is not empty, take one point from queue, enlarge neighbor point
  # and put into queue

  while queue:
    node = queue.popleft()
    # if we have destination point, we can add a check here
    if node is last_point:
      break or return something
    for neighbor in node.get_neighbors():
      if neighbor in distance:
        continue
      queue.append(neighbor)
      distance[neighbor] = distance[node] + 1
    # if need all points to starting point distance, return hashMap
    return distance
    # if need all connecting point, return points in hashMap
    return distance.keys()
