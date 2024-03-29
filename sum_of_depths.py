def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack):
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]

        if node is None:
            continue
        
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sumOfDepths


def nodeDepthsRec(root, depth = 0):
    if root is None:
        return 0

    return depth + nodeDepthsRec(root.left, depth + 1) + nodeDepthsRec(root.right, depth + 1)