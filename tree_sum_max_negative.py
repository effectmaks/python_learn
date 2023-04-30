"""
Поиск по дереву максимальной суммы положительных и отрицательных чисел
DFS - поиск в глубину?
Время выполнения Time:O(n) - пройти по каждому элементу
Сложность обработки алгоритма по памяти Space: O(n) - В стеке рекурсии будут все вершины от дерева
"""


class Item:
    def __init__(self, value, left: 'Item' = None, right: 'Item' = None):
        self.value: int = value
        self.left = left
        self.right = right


item_a = Item(-2)
item_b = Item(5, left=item_a)
item_c = Item(4)
item_d = Item(-2)
item_e = Item(-3, left=item_b, right=item_c)
item_f = Item(8, right=item_d)
item_h = Item(9)
item_g = Item(20, left=item_e, right=item_f)
item_e = Item(-10, left=item_h, right=item_g)


class Solution:
    def __init__(self):
        self.answer: int = 0

    def find_sum_ng(self, item: Item):
        self._calc(item)
        return self.answer

    def _calc(self, item: Item):
        if item is None:
            return 0

        sum_left = max(self._calc(item.left), 0)  # Если сумма отрицательна, значит ветка не нужна
        sum_right = max(self._calc(item.right), 0)  # -||-
        self.answer = max(self.answer, sum_left + sum_right + item.value)
        return max(sum_left, sum_right) + item.value


sol = Solution()
print("find_sum_ng", sol.find_sum_ng(item_e))




















