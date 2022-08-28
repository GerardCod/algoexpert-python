def getNthFib(n):
    table = dict()

    return getNthFibAux(n, table)


def getNthFibAux(n, table):
    if n == 2:
        return 1
    
    if n == 1:
        return 0
    
    if n in table:
        return table[n]
    
    table[n] = getNthFibAux(n - 1, table) + getNthFibAux(n - 2, table)
    return table[n]



if __name__ == '__main__':
  print(getNthFib(6))