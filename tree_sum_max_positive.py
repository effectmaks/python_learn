"""
Поиск по дереву максимальной суммы положительных чисел
Тривиальный случай - если ячейка пустая
Время выполнения Time:O(n) - пройти по каждому элементу
Сложность обработки алгоритма по памяти Space: O(n) - В стеке рекурсии будут все вершины от дерева
"""


class Item:
    def __init__(self, value, item_left: 'Item' = None, item_right: 'Item' = None):
        self.value: int = value
        self.item_left = item_left
        self.item_right = item_right


item_a = Item(2)
item_b = Item(2)
item_c = Item(3, item_right=item_a)
item_d = Item(5)
item_e = Item(4)
item_f = Item(4, item_left=item_b, item_right=item_c)
item_g = Item(7, item_left=item_d, item_right=item_e)
item_h = Item(1, item_left=item_f, item_right=item_g)


def find_sum(item: Item):
    if item is None:  # Тривиальный случай
        return 0
    sum_left = find_sum(item.item_left)
    sum_right = find_sum(item.item_right)
    return max(sum_left, sum_right) + item.value


print(find_sum(item_h))
