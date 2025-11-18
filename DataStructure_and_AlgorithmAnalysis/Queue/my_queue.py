class Queue(object):
    """将列表实现为队列"""

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)
