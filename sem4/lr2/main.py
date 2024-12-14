"""
Иванов Никита 1.1
Лабораторная работа 2.

Реализовать нерекурсивный вариант функции для построения бинарного дерева.

"""
def gen_bin_tree(height: int, root: int) -> dict:
    """
    Генерирует бинарное дерево заданной высоты с заданным корнем.

          Параметры:
            height (int): высота дерева (количество уровней дерева, не включая корень).
            root (int): значение корня дерева.

          Возвращаемое значение:
            tree (dict): бинарное дерево в виде словаря, 
            где ключи - значения узлов,а значения - списки.
    """
    if not isinstance(height, (int)) or not isinstance(root, (int)):
        raise TypeError("Введены неверные значения")
      
    if height < 0:
      raise ValueError("Введена отрицательная высота")
      
    tree = {str(root): []}

    
    if height == 0:
      return tree
    
      
    roots = [[root]]

    for l in range(1, height + 1):
        if len(roots) == 1:
            _r = roots[-1]
        else:
            _r = [item for sublist in roots[-1] for item in sublist]


        leaves = list(map(lambda r: [r + 2 , r * 3], _r))


        roots.append(leaves)
        
    roots.reverse()
    roots.pop()
    
    roots[0] = list(map(lambda x: [{str(x[0]): []}, {str(x[1]): []}], roots[0]))
    
    for i in range(len(roots)):
      queue = roots[i]
      for j in range(len(queue)//2):
        child1=queue.pop(0)
        child2=queue.pop(0)
        roots[i+1][j][0] = {str(roots[i+1][j][0]):child1}
        roots[i+1][j][1] = {str(roots[i+1][j][1]):child2}
        
    tree[str(root)].extend(roots[-1][0])
    return tree

if __name__ == '__main__':
    import pprint
    pprint.pprint(gen_bin_tree(4, 3))
