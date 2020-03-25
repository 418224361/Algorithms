class Node:
    def __init__(self, key, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next


class Link:
    def __init__(self, head=None):
        self.head = head

    def search(self, key):
        x = self.head
        while x is not None and x.key != key:
            x = x.next
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

    def delete_key(self, key):
        node = self.search(key)
        if not node:
            raise ValueError('{} not exist'.format(key))
        self.delete_node(node)
