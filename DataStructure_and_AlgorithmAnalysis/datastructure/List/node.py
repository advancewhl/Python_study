class Node(object):
    """一个链表节点"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """获取节点数据"""
        return self._data

    def set_data(self, node_data):
        """设置节点数据"""
        self._data = node_data

    data = property(get_data, set_data)

    def set_next(self, node_next):
        """设置下一个节点"""
        self._next = node_next

    def get_next(self):
        """获取下一个节点"""
        return self._next

    next = property(get_next, set_next)

    def __str__(self):
        """字符串"""
        return str(self.get_data())
