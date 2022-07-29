
class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def addToBst(bst, value):
    if bst.value > value and bst.left is None:
        bst.left = BinaryTree(value)
        return
    
    if bst.value < value and bst.right is None:
        bst.right = BinaryTree(value)
        return

    if bst.value > value:
        addToBst(bst.left, value)

    if bst.value < value:
        addToBst(bst.right, value)


def getTreeHeight(bst):
    if bst is None:
        return 0

    leftHeight = getTreeHeight(bst.left) + 1
    rightHeight = getTreeHeight(bst.right) + 1

    return max(leftHeight, rightHeight)
        
    
def levelOrderTraversalHeight(bst):
    for level in range(1, getTreeHeight(bst)):
        printCurrentLevel(bst, level)


def levelOrderTraversalBool(bst):
    level = 1

    while printCurrentLevelBool(bst, level):
        level += 1


def printCurrentLevelBool(bst, level):
    if bst is None:
        return False

    if level == 1:
        print(bst.value, sep=" ")
        return True

    left = printCurrentLevelBool(bst.left, level - 1)
    right = printCurrentLevelBool(bst.right, level - 1)
    return left or right

def printCurrentLevel(bst, level):
    if bst is None:
        return
    if level == 1:
        print(bst.value)
    elif level > 1:
        printCurrentLevel(bst.left, level - 1)
        printCurrentLevel(bst.right, level - 1)

if __name__ == '__main__':
    bst = BinaryTree(5)
    addToBst(bst, 4)
    addToBst(bst, 10)
    addToBst(bst, 2)
    addToBst(bst, 9)
    addToBst(bst, 8)
    addToBst(bst, 12)

    #levelOrderTraversalBool(bst)