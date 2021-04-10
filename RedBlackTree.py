from enum import Enum
from random import randint


class Color(Enum):
    RED = 1
    BLACK = 0


class Node:
    def __init__(self, value, color, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
        self.color = color

    def __repr__(self):
        return f'({self.value}, {self.color})'


class RedBlackTree:
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None

    def print(self, node, space, file):
        if not node:
            print(space, 'NIL', file=file)
            return
        print(space, node, file=file)
        self.print(node.left, space + '-', file)
        self.print(node.right, space + '-', file)

    def insert(self, value):
        if not self.root:
            self.root = Node(value, Color.BLACK)
        else:
            self._insert(self.root, value)

    def search(self, value):
        if not self.root:
            return False
        return self._search(self.root, value)

    def _insert(self, node, value):
        if value <= node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value, Color.RED, parent=node)
                self._balance(node)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value, Color.RED, parent=node)
                self._balance(node)

    def _search(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        if value <= node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def _rotate_left(self, node):
        left_son = node.left
        parent = node.parent
        gr_parent = node.parent.parent
        my_position = 0
        if gr_parent and parent is gr_parent.right:
            my_position = 1
        if gr_parent and parent is gr_parent.left:
            my_position = 2
        node.left = parent
        parent.right = left_son
        parent.parent = node
        if left_son:
            left_son.parent = parent
        node.parent = gr_parent
        node.color = Color.BLACK
        node.left.color = Color.RED
        node.right.color = Color.RED
        if my_position == 1:
            gr_parent.right = node
        elif my_position == 2:
            gr_parent.left = node
        else:
            self.root = node

    def _rotate_right(self, node):
        right_son = node.right
        parent = node.parent
        gr_parent = node.parent.parent
        my_position = 0
        if gr_parent and parent is gr_parent.right:
            my_position = 1
        if gr_parent and parent is gr_parent.left:
            my_position = 2
        node.right = parent
        parent.parent = node
        parent.left = right_son
        if right_son:
            right_son.parent = parent
        node.parent = gr_parent
        node.color = Color.BLACK
        node.left.color = Color.RED
        node.right.color = Color.RED
        if my_position == 1:
            gr_parent.right = node
        elif my_position == 2:
            gr_parent.left = node
        else:
            self.root = node

    def _balance(self, node):
        # Если нет вершины - выходим
        if not node:
            return
        # Если вершина черного цвета - все хорошо
        if node.color == Color.BLACK:
            return
        # Если вершина красная и является корнем - просто перекрашиваем
        if not node.parent:
            node.color = Color.BLACK
            return
        # Ищем дядю и в зависимости от его цвета проверяем 2 ситуации
        uncle = node.parent.right
        if node is node.parent.right:
            uncle = node.parent.left
        # Если дядя красный - перекрашиваем себя и его в черный, а деда в красный и запускаем балансировку от деда
        if uncle and uncle.color == Color.RED:
            uncle.color = Color.BLACK
            node.color = Color.BLACK
            node.parent.color = Color.RED
            if node.parent.parent:
                self._balance(node.parent.parent)
            else:
                node.parent.color = Color.BLACK
            return
        # Если дяди нет или он черный - надо делать поворот
        if not uncle or uncle.color == Color.BLACK:
            # Если мы находимся справа от деда, а наш сын слева - меняем себя местами с сыном
            if node is node.parent.right:
                if node.left and node.left.color == Color.RED:
                    x = node.left
                    x.parent = node.parent
                    node.left = x.right
                    if x.right:
                        x.right.parent = node
                    x.right = node
                    node.parent = x
                    self._rotate_left(x)
                else:
                    self._rotate_left(node)
            # Если мы находимся слева от деда, а наш сын справа - меняем себя местами с сыном
            else:
                if node is node.parent.left:
                    if node.right and node.right.color == Color.RED:
                        x = node.right
                        x.parent = node.parent
                        node.right = x.left
                        if x.left:
                            x.left.parent = node
                        x.left = node
                        node.parent = x
                        self._rotate_right(x)
                    else:
                        self._rotate_right(node)


rbt = RedBlackTree()
