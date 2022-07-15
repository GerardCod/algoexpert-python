class BinaryTree:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None


def branchSums(tree):
    sums = []
    calculateBranchSums(tree, 0, sums)
    return sums


def calculateBranchSums(tree, currentSum, sums):
    """
      Calcula la suma de las ramas de un árbol binario.
      recorre el un árbol binario hasta llegar a los nodos hoja y guardar la suma
      de cada rama en una lista.
    """
    if tree is None:
      return

    newCurrentSum = tree.value + currentSum

    if tree.left is None and tree.right is None:
      sums.append(newCurrentSum)
      return
    
    calculateBranchSums(tree.left, newCurrentSum, sums)
    calculateBranchSums(tree.right, newCurrentSum, sums)



