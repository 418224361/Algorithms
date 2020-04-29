# 10-2 利用链表实现可合并堆
from Introduction_To_Algorithms.第10章_基本数据结构.C10_4_有根树的表示 import Node
from Introduction_To_Algorithms.第10章_基本数据结构.C10_4_有根树的表示 import BinaryTree


class Heap(BinaryTree):
    def __init__(self, nodes_list):
        nodes = [Node(nodes_list[i]) for i in range(len(nodes_list))]
        super().__init__(nodes)

    def left(self, p, l, r):
        if r:
            r.parent = l
        if l.right:
            l.right.parent = p
        if l.left:
            l.left.parent = p
        p.right, l.right = l.right, p.right
        p.left = l.left
        l.left = p
        if p == self.root:
            self.root = l
        elif p == p.parent.left:
            p.parent.left=l
        else:
            p.parent.right = l
        l.parent = p.parent
        p.parent = l
        return l, p, r

    def right(self, p, l, r):
        if l:
            l.parent = r
        if r.right:
            r.right.parent = p
        if r.left:
            r.left.parent = p
        p.left, r.left = r.left, p.left
        p.right = r.right
        r.right = p
        if p == self.root:
            self.root = r
        elif p == p.parent.left:
            p.parent.left = r
        else:
            p.parent.right = r
        r.parent = p.parent
        p.parent = r
        return r, l, p

    def max_heapify(self, current_node=None, method=1):
        """
        假设current_node的左子树和右子树都已经是最大堆
        :param method: 1:改变node节点的指针，不改变node节点的value。速度慢，但不改变节点对象的值
                       0:不改变node节点的指针，改变node节点的value。速度快，但会改变节点对象的值。
                       默认为1
        :param current_node: 堆的待排序节点
        :return: 基于假设的最大堆
        """
        if current_node is None:
            current_node = self.root
        if self.isleaf(current_node):
            return
        p = current_node
        l = current_node.left
        r = current_node.right
        if method == 0:
            if r:
                # 左孩子比父亲和右孩子大
                if l.value > p.value and l.value > r.value:
                    l.value, p.value = p.value, l.value
                    self.max_heapify(l)
                # 右孩子比父亲和左孩子大
                elif r.value > p.value and r.value > l.value:
                    r.value, p.value = p.value, r.value
                    self.max_heapify(r)
            # 左孩子比父亲大，没有右孩子
            elif l.value > p.value:
                l.value, p.value = p.value, l.value
                self.max_heapify(l)
        elif method == 1:
            if r:
                # 左孩子比父亲和右孩子大
                if l.value > p.value and l.value > r.value:
                    _, current_node, _ = self.left(p, l, r)
                    self.max_heapify(current_node)
                # 右孩子比父亲和左孩子大
                elif r.value > p.value and r.value > l.value:
                    _, _, current_node = self.right(p, l, r)
                    self.max_heapify(current_node)
            # 左孩子比父亲大，没有右孩子
            elif l.value > p.value:
                _, current_node, _ = self.left(p, l, r)
                self.max_heapify(current_node)
        else:
            raise ValueError('method只能取0或1')


h = Heap([1, 2, 3, 0])
h.max_heapify(method=0)
print(h.root.value)
print(h.root.left.value)
print(h.root.right.value)
print(h.root.left.left.value)
# print(h.root.left.right.value)
print(h.walkman())
