class Node:
    def __init__(self, key, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class Link:
    def __init__(self, head=None, *args):
        self.head = head
        for arg in args:
            self.insert(arg)

    def search(self, key):
        x = self.head
        while x is not None and x.key != key:
            x = x.next
        if x is None:
            raise ValueError('{} not exists'.format(key))
        return x

    def insert(self, node):
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        node.prev = None

    def delete_node(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next is not None:
            node.next.prev = node.prev

    def delete_key(self, key):  # 根据Node节点的关键字删除Node节点
        node = self.search(key)
        if not node:
            raise ValueError('{} not exists'.format(key))
        self.delete_node(node)

    def __len__(self):
        size = 0
        x = self.head
        while x is not None:
            size += 1
            x = x.next
        return size

    def iter(self):  # 迭代显示link的所有node节点
        x = self.head
        for i in range(len(self)):
            yield x
            x = x.next


class SingleLink(Link):
    def insert(self, node):
        node.next = self.head
        self.head = node

    def delete_node(self, node):
        x = self.head
        if x == node:
            self.head = x.next
        else:
            while x is not None and x.next != node:
                x = x.next
            if x is None:
                raise IndexError('{} not exists'.format(node.key))
            x.next = node.next

    def delete_key(self, key):
        x = self.head
        if x.key == key:
            self.head = x.next
        else:
            while x is not None and x.next.key != key:
                x = x.next
            if x is None:
                raise IndexError('{} not exits'.format(key))
            x.next = x.next.next


# 练习10.2-2 用单链表实现一个栈，要求push和pop操作时间是O(1)
class LinkStack(SingleLink):
    def push(self, node):
        return super().insert(node)

    def pop(self):
        x = self.head
        super().delete_node(x)
        return x


# 练习10.2-3 用单链表实现一个队列，要求enqueue和dequeue操作时间是O(1)


if __name__ == '__main__':
    node1 = Node(9, '9')
    node2 = Node(16, '16')
    node3 = Node(4, '4')
    node4 = Node(1, '1')
    node5 = Node(25, '25')

    link = Link(node1, node2, node3, node4)
    for node in link.iter():
        print(node.value)
    print('-' * 10)

    link.insert(node5)
    for node in link.iter():
        print(node.value)
    print('-' * 10)

    link.delete_node(node3)
    for node in link.iter():
        print(node.value)
    print('-' * 10)

    link.delete_key(1)
    for node in link.iter():
        print(node.value)

    stack = LinkStack(node1, node2, node3, node4)
    for node in stack.iter():
        print(node.key)
    print('-' * 10)

    stack.push(node5)
    for node in stack.iter():
        print(node.value)
    print('-' * 10)

    stack.pop()
    for node in stack.iter():
        print(node.value)
    print('-' * 10)

    x = stack.pop()
    for node in stack.iter():
        print(node.value)
    print('key is {}'.format(x.key))
