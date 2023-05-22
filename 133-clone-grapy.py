from typing import List


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}

        def clone(node):
            if node in visited:
                return visited[node]

            clone_node = Node(node.val)
            visited[node] = clone_node

            if node.neighbors:
                clone_node.neighbors = [clone(n) for n in node.neighbors]

            return clone_node

        return clone(node)


def createGraph(input_list):
    # Create a dictionary to store the mapping between node values and their corresponding nodes
    node_dict = {}

    # Iterate through each sub-list in input_list and create a node for each unique value
    for sublist in input_list:
        for value in sublist:
            if value not in node_dict:
                node = Node(value)
                node_dict[value] = node

    # Iterate through each sub-list in input_list and connect the corresponding nodes in the graph
    for sublist in input_list:
        node1 = node_dict[sublist[0]]
        node2 = node_dict[sublist[1]]
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

    # Return the starting node of the graph
    return node_dict[input_list[0][0]]


# Example usage
input_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
solution = Solution()
graph_node = createGraph(input_list)
cloned_graph_node = solution.cloneGraph(graph_node)
print(cloned_graph_node.val)
