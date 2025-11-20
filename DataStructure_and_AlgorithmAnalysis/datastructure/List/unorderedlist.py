from node import Node


class UnorderedList(object):
    """构造无序列表"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError(f"{item} is not in the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def append(self, item):
        temp = Node(item)
        if self.head is None:
            self.head = temp
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = temp

    def insert(self, pos, item):
        length = self.size()
        # 处理负索引：-1 表示倒数第一项前
        if pos < 0:
            pos += length
        if pos < 0 or pos > length:
            raise IndexError("index out of range")

        node = Node(item)
        if pos == 0:
            node.next = self.head
            self.head = node
            return

        current = self.head
        for _ in range(pos - 1):
            current = current.next
            if current is None:
                raise IndexError("index out of range")

        node.next = current.next
        current.next = node

    def index(self, item):
        count = 0
        current = self.head
        while current is not None:
            if current.data == item:
                return count
            current = current.next
            count += 1
        raise ValueError(f"{item} is not in list")

    def pop(self, pos=-1):
        if self.head is None:
            raise IndexError(f"pop from empty list")
        length = self.size()
        if pos < 0:
            pos += length
        if pos < 0 or pos >= length:
            raise IndexError(f"{pos} is beyond the list")
        current = self.head
        previous = None
        if pos == 0:
            self.head = current.next
            return current.data
        for _ in range(pos):
            previous = current
            current = current.next
        previous.next = current.next
        return current.data
