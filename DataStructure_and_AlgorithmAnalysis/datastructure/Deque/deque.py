class Deque(object):
    """将列表实现为双端队列"""

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def add_rear(self, item):
        self._items.insert(0, item)

    def add_front(self, item):
        self.items.append(item)

    def remove_front(self):
        self._items.pop()

    def remove_rear(self):
        self._items.pop(0)

    def size(self):
        return len(self._items)
