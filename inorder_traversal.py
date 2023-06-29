def inorder_traversal(root):
    if root is None:
        return []

    # create a dummy node, right pointer to root
    # and put it in stack, now stack head is dummy
    # iterator current position

    dummy = TreeNode(0)
    dummy.right = root
    stack = [dummy]
    inorder = []

    # move iterator to next point
    # which is adjust stack head and move it to next point

    while stack:
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        if stack:
            inorder.append(stack[-1])
        return inorder
