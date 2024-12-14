def gen_bin_tree(height=5, root=10, left=lambda r: r + 2, right=lambda r: r * 3):
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




def gen_bin_tree_recursion(height=5, root=10, left=lambda r: r + 2, right=lambda r: r * 3):
    tree = {str(root): []}

    if height == 0:
        return tree

    return {
        str(root): [
            gen_bin_tree_recursion(height - 1,
                         left(root),
                         left=left,
                         right=right),
            gen_bin_tree_recursion(height - 1,
                         left(root),
                         left=left,
                         right=right)
        ]
    }

