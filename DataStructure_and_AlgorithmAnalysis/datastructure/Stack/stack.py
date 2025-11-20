class Stack(object):
    """栈数据结构"""

    def __init__(self):
        """创建新栈"""
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        a = self.items.pop()
        return a

    def peek(self):
        item_last = self.items[-1]
        return item_last

    def is_empty(self):
        # if self.items:
        #     return False
        # else:
        #     return True
        # returm self.items == []
        return not bool(self.items)

    def size(self):
        return len(self.items)


# s = Stack()
# print(s.is_empty())
# s.push(4)
# s.push("dog")
# print(s.peek())
# s.push(True)
# print(s.size())
# s.push(9.8)
# print(s.pop())
# print(s.pop())
# print(s.size())
