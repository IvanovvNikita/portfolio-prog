"""
Иванов Никита 1.1 
Лабораторная работа 1.

Реализовать рекурсивный вариант функции для построения бинарного дерева.

Root = 3; height = 4, left_leaf = root+2, right_leaf = root*3
"""


def gen_bin_tree(height: int,
                 root: int,
                 left_l_func=lambda r: r + 2,
                 right_l_func=lambda r: r * 3) -> dict:
    """
    Рекурсивная функция создания бинарного дерева

    
    """
    
    tree = {str(root): []}

    if height == 0:
        return tree
    # TODO Подумать об оптимизации использования переменных # tree[root].append()
    # append ставил лишние [], которые тяжело было учитывать при тестах, поэтому я нашел и     воспользовался extend
    tree[str(root)].extend([gen_bin_tree(height - 1,
                         left_l_func(root),
                         left_l_func=left_l_func,
                         right_l_func=right_l_func),
            gen_bin_tree(height - 1,
                         right_l_func(root),
                         left_l_func=left_l_func,
                         right_l_func=right_l_func)])
    return tree    


if __name__ == '__main__':
    import pprint  

    pprint.pprint(
        gen_bin_tree(height=4,
                     root=3,
                     left_l_func=lambda r: r + 2,
                     right_l_func=lambda r: r * 3))
