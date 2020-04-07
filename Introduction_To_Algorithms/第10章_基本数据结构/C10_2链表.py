# 带有前驱和后继的节点
class Node:
    def __init__(self, key, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


# 带有后继而无前驱的节点
class SingleNode:
    def __init__(self, key, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


# 双向链表
class Link:
    def __init__(self, *args):
        self.head = None  # self.head表示链表的第一个元素
        self._length = 0
        for arg in args:
            self.insert(arg)

    def search(self, key):
        # 查找列表中第一个关键字为key的元素，返回节点对象
        x = self.head
        while x is not None and x.key != key:
            x = x.next
        if x is None:
            raise ValueError('Error search! {} not exists'.format(key))
        return x

    def insert(self, node):
        # 链表前端插入一个元素，支持对非空链表查重
        x = self.head
        while x is not None:
            if id(x) == id(node):
                raise ValueError('Identical node, key={}'.format(node.key))
            x = x.next

        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        node.prev = None
        self._length += 1

    def delete(self, node):
        # 从链表中删除一个元素
        # 首先检查待删除元素是否在链表中
        count = len(self)
        if count == 0:
            return ValueError('Empty link')
        exist = False
        x = self.head
        while x is not None and count > 0:
            if id(x) == id(node):
                exist = True
                break
            x = x.next
            count -= 1
        if exist is False or count == 0:
            raise ValueError('Error deletion, {} not exists in link'.format(node.key))

        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev
        self._length -= 1

    def delete_key(self, key):
        # 根据关键字删除元素
        # 首先检查待删除元素是否在链表中
        count = len(self)
        if count == 0:
            return ValueError('Empty link')
        exist = False
        x = self.head
        while x is not None and count > 0:
            if x.key == key:
                exist = True
                break
            x = x.next
            count -= 1
        if exist is False or count == 0:
            raise ValueError('Error deletion, {} not exists in link'.format(key))

        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev
        self._length -= 1

    def __len__(self):
        return self._length

    def iter(self):
        # 迭代显示链表的所有元素
        if self._length == 0:
            return None
        x = self.head
        for i in range(len(self)):
            yield x
            x = x.next


# 单链表
class SingleLink(Link):
    def insert(self, node):
        # 非空链表查重
        x = self.head
        while x is not None:
            if id(x) == id(node):
                raise ValueError('Identical node, key={}'.format(node.key))
            x = x.next

        node.next = self.head
        self.head = node
        self._length += 1

    def delete(self, node):
        count = len(self)
        if count == 0:
            return ValueError('Empty link')
        # x是待删除元素的上一个元素
        x = self.head
        if x is None:
            raise ValueError('Empty link')
        elif x == node:
            self.head = x.next
        else:
            while x is not None and x.next != node and count > 0:
                x = x.next
                count -= 1
            if x is None or count == 0:
                raise IndexError('Error deletion! {} not exists in link'.format(node.key))
            x.next = node.next
        self._length -= 1

    def delete_key(self, key):
        count = len(self)
        if count == 0:
            return ValueError('Empty link')
        # x是待删除元素的上一个元素
        x = self.head
        if x is None:
            raise ValueError('Empty link')
        elif x.key == key:
            self.head = x.next
        else:
            while x is not None and x.next.key != key and count > 0:
                x = x.next
                count -= 1
            if x is None or count == 0:
                raise IndexError('Error deletion! {} not exits in link'.format(key))
            x.next = x.next.next
        self._length -= 1


# 带哨兵的双向链表
class SentinelLink:
    def __init__(self, *args):
        self.sentinel = Node(None, None, None, None)  # self.sentinel的下一个元素是链表的首元素
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self._length = 0
        for arg in args:
            self.insert(arg)

    def search(self, key):
        x = self.sentinel.next
        while x is not self.sentinel and x.key != key:
            x = x.next
        if x is self.sentinel:
            raise ValueError('Error search! {} not exists'.format(key))
        return x

    def insert(self, node):
        # 非空链表查重
        x = self.sentinel.next
        while x is not self.sentinel:
            if id(x) == id(node):
                raise ValueError('Identical node, key={}'.format(node.key))
            x = x.next

        self.sentinel.next.prev = node
        node.next = self.sentinel.next
        node.prev = self.sentinel
        self.sentinel.next = node
        self._length += 1

    def delete(self, node):
        count = len(self)
        if count == 0:
            return ValueError('Empty link')
        # x是待删除元素的上一个元素
        x = self.sentinel.next
        while x is not self.sentinel and x != node and count > 0:
            x = x.next
            count -= 1
        if x is self.sentinel or count == 0:
            raise ValueError('Error deletion! {} not exists'.format(node.key))
        x.prev.next = x.next
        x.next.prev = x.prev
        self._length -= 1

    def delete_key(self, key):
        count = len(self)
        if count == 0:
            return ValueError('Empty link')
        # x是待删除元素的上一个元素
        x = self.sentinel.next
        while x is not self.sentinel and x.key != key and count > 0:
            x = x.next
            count -= 1
        if x is self.sentinel or count == 0:
            raise ValueError('Error deletion! {} not exists in link'.format(key))
        x.prev.next = x.next
        x.next.prev = x.prev
        self._length -= 1

    def __len__(self):
        return self._length

    def iter(self):  # 迭代显示link的所有node节点
        if self._length == 0:
            return None
        x = self.sentinel.next
        while x is not self.sentinel:
            yield x
            x = x.next


# 带哨兵的单链表
class SentinelSingleLink(SentinelLink):
    def __init__(self, *args):
        self.sentinel = SingleNode(None, None, None)  # self.sentinel的下一个元素是链表的首元素
        self.sentinel.next = self.sentinel
        self._length = 0
        for arg in args:
            self.insert(arg)

    def insert(self, node):
        # 非空链表查重
        x = self.sentinel.next
        while x is not self.sentinel:
            if id(x) == id(node):
                raise ValueError('Identical node, key={}'.format(node.key))
            x = x.next

        node.next = self.sentinel.next
        self.sentinel.next = node
        self._length += 1

    def delete(self, node):
        count = len(self)
        if count == 0:
            return ValueError('Empty link')
        # x是待删除元素的上一个元素
        x = self.sentinel
        while x.next is not self.sentinel and x.next != node and count > 0:
            x = x.next
            count -= 1
        if x.next is self.sentinel or count == 0:
            raise ValueError('Error deletion! {} not exists'.format(node.key))
        x.next = x.next.next
        self._length -= 1

    def delete_key(self, key):
        count = len(self)
        if count == 0:
            return ValueError('Empty link')
        # x是待删除元素的上一个元素
        x = self.sentinel
        while x.next is not self.sentinel and x.next.key != key and count > 0:
            x = x.next
            count -= 1
        if x.next is self.sentinel or count == 0:
            raise ValueError('Error deletion! {} not exists'.format(key))
        x.next = x.next.next
        self._length -= 1


# 练习10.2-2 用单链表实现一个栈，要求push和pop操作时间是O(1)
class LinkStack(SingleLink):
    def push(self, node):
        return super().insert(node)

    def pop(self):
        x = self.head
        super().delete(x)
        return x


# 练习10.2-3 用单链表实现一个队列，要求enqueue和dequeue操作时间是O(1)
class LinkQueue(Link):
    def __init__(self, *args):
        self.head = None  # 链表的第一个元素
        self.tail = None  # 链表的最后一个元素
        self.pretail = None  # 链表的倒数第二个元素
        self._length = 0
        for arg in args:
            self.enqueue(arg)

    def enqueue(self, node):
        # 非空链表查重
        x = self.head
        while x is not None:
            if id(x) == id(node):
                raise ValueError('Identical node, key={}'.format(node.key))
            x = x.next
        # 记录链表的最后一个元素
        if self.head is None:
            self.tail = node
        # 记录链表的倒数第二个元素
        elif self.head.next is None:
            self.pretail = node
        node.next = self.head
        self.head = node
        self._length += 1

    def dequeue(self):
        if len(self) == 0:
            raise ValueError('Empty queue')
        x = self.tail
        self.pretail.next = None
        self._length -= 1
        return x


if __name__ == '__main__':
    node1 = Node(1, '1')
    node2 = Node(2, '2')
    node3 = Node(3, '3')
    node4 = Node(4, '4')
    node5 = Node(5, '5')
    node100 = Node(100, '100')

    snode1 = SingleNode(1, '1')
    snode2 = SingleNode(2, '2')
    snode3 = SingleNode(3, '3')
    snode4 = SingleNode(4, '4')
    snode5 = SingleNode(5, '5')
    snode100 = SingleNode(100, '100')

    print('--Link--')
    link = Link(node1, node2, node3, node4)
    for _node in link.iter():
        print(_node.value, end=',')
    print('\n')

    link.insert(node5)
    for _node in link.iter():
        print(_node.value, end=',')
    print('\n')

    link.delete(node3)
    for _node in link.iter():
        print(_node.value, end=',')
    print('\n')

    link.delete_key(4)
    for _node in link.iter():
        print(_node.value, end=',')
    print('\n')

    print(id(link.search(5)) == id(node5))

    link.delete_key(5)
    link.delete_key(2)
    for _node in link.iter():
        print(_node.value, end=',')
    print('\n')
    link.delete_key(1)
    for _node in link.iter():
        print(_node.value, end=',')
    print('\n')

    print('--SingleLink--')
    singlelink = SingleLink(snode1, snode2, snode3, snode4)
    for _node in singlelink.iter():
        print(_node.value, end=',')
    print('\n')

    singlelink.insert(snode5)
    for _node in singlelink.iter():
        print(_node.value, end=',')
    print('\n')

    singlelink.delete(snode3)
    for _node in singlelink.iter():
        print(_node.value, end=',')
    print('\n')

    singlelink.delete_key(4)
    for _node in singlelink.iter():
        print(_node.value, end=',')
    print('\n')

    print(id(singlelink.search(5)) == id(snode5))

    singlelink.delete_key(5)
    singlelink.delete_key(2)
    for _node in singlelink.iter():
        print(_node.value, end=',')
    print('\n')
    singlelink.delete_key(1)
    for _node in singlelink.iter():
        print(_node.value, end=',')
    print('\n')

    print('--SentinelLink--')
    sentinellink = SentinelLink(node1, node2, node3, node4)
    for _node in sentinellink.iter():
        print(_node.value, end=',')
    print('\n')

    sentinellink.insert(node5)
    for _node in sentinellink.iter():
        print(_node.value, end=',')
    print('\n')

    sentinellink.delete(node3)
    for _node in sentinellink.iter():
        print(_node.value, end=',')
    print('\n')

    sentinellink.delete_key(4)
    for _node in sentinellink.iter():
        print(_node.value, end=',')
    print('\n')

    print(id(sentinellink.search(5)) == id(node5))

    sentinellink.delete_key(5)
    sentinellink.delete_key(2)
    for _node in sentinellink.iter():
        print(_node.value, end=',')
    print('\n')
    sentinellink.delete_key(1)
    for _node in sentinellink.iter():
        print(_node.value, end=',')
    print('\n')

    print('--SentineSinglelLink--')
    sentinelsinglelink = SentinelSingleLink(snode1, snode2, snode3, snode4)
    for _node in sentinelsinglelink.iter():
        print(_node.value, end=',')
    print('\n')

    sentinelsinglelink.insert(snode5)
    for _node in sentinelsinglelink.iter():
        print(_node.value, end=',')
    print('\n')

    sentinelsinglelink.delete(snode3)
    for _node in sentinelsinglelink.iter():
        print(_node.value, end=',')
    print('\n')

    sentinelsinglelink.delete_key(4)
    for _node in sentinelsinglelink.iter():
        print(_node.value, end=',')
    print('\n')

    print(id(sentinelsinglelink.search(5)) == id(snode5))

    sentinelsinglelink.delete_key(5)
    sentinelsinglelink.delete_key(2)
    for _node in sentinelsinglelink.iter():
        print(_node.value, end=',')
    print('\n')
    sentinelsinglelink.delete_key(1)
    for _node in sentinelsinglelink.iter():
        print(_node.value, end=',')
    print('\n')

    print('--LinkStack--')
    stack = LinkStack(node1, node2, node3, node4)
    for _node in stack.iter():
        print(_node.value, end=',')
    print('\n')

    stack.push(node5)
    for _node in stack.iter():
        print(_node.value, end=',')
    print('\n')

    stack.pop()
    for _node in stack.iter():
        print(_node.value, end=',')
    print('\n')

    x = stack.pop()
    for _node in stack.iter():
        print(_node.value, end=',')
    print('\n')
    print(x.key)
    print('\n')

    print('--LinkQueue--')
    lq = LinkQueue(snode1, snode2, snode3, snode4)
    for node in lq.iter():
        print(node.key, end=',')
    print('\n')
    lq.enqueue(node5)
    lq.dequeue()
    for node in lq.iter():
        print(node.key, end=',')
