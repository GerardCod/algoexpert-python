def closest_value(bst, target):
    closest = float("inf")

    while bst is not None:
        current_span = abs(target - bst.value)

        if abs(target - closest) > current_span:
            closest = bst.value
        
        if target < bst.value:
            bst = bst.left
        elif target > bst.value:
            bst = bst.right
        else:
            break

    return closest

def findClosestValue(tree, target):
    return findClosestValueHelper(tree, target, float("inf"))


def findClosestValueHelper(tree, target, closest):
    if tree is None:
        return closest
    
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueHelper(tree.right, target, closest)
    else:
        return closest  


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addNode(self, node):
        if node.value > self.value and self.right is None:
            self.right = node
        
        if node.value < self.value and self.left is None:
            self.left = node

        if node.value > self.value:
            self.addNode(self.right, node)
        elif node.value < self.value:
            self.addNode(self.left, node)


if __name__ == '__main__':
    tree = BST(10)
    tree.addNode(BST(12))