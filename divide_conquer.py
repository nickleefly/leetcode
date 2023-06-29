def divide_conquer(root):
# check node == null
# in most cases, no need to do node == leaf

if root is None:
  return ...

# do left tree
left_result = divide_conquer(node.left)

# do right tree
right_result = divide_conquer(node.right)

# merge resule
result = merge left_result and right_result # to get merged result
return result
