# 10-2 利用链表实现可合并堆
import math
from 第10章_基本数据结构.C10_4_有根树的表示 import Node
from 第10章_基本数据结构.C10_4_有根树的表示 import BinaryTree


class Heap(BinaryTree):
    def __init__(self, nodes_list):
        self.nodes = [Node(nodes_list[i]) for i in range(len(nodes_list))]
        super().__init__(self.nodes)

    def _left(self, p, l, r):
        """
        父节点p，左节点l，右节点r
        左节点最大时，交换父节点和左节点位置(实际是交换他们的parent, left_child和right_child)
        """
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
            p.parent.left = l
        else:
            p.parent.right = l
        l.parent = p.parent
        p.parent = l
        return l, p, r

    def _right(self, p, l, r):
        """
        父节点p，左节点l，右节点r
        右节点最大时，交换父节点和右节点位置(实际是交换他们的parent, left_child和right_child)
        """
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

    def _max_heapify(self, current_node=None, method=0):
        """
        假设current_node的左子树和右子树都已经是最大堆
        :param method: 0:不改变node节点的指针，改变node节点的value。速度快，但会改变节点对象的值，换药不换汤。
                       1:改变node节点的指针，不改变node节点的value。速度慢，但不改变节点对象的值
                       默认为0
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
                    self._max_heapify(l)
                # 右孩子比父亲和左孩子大
                elif r.value > p.value and r.value > l.value:
                    r.value, p.value = p.value, r.value
                    self._max_heapify(r)
            # 左孩子比父亲大，没有右孩子
            elif l.value > p.value:
                l.value, p.value = p.value, l.value
                self._max_heapify(l)
        elif method == 1:
            if r:
                # 左孩子比父亲和右孩子大
                if l.value > p.value and l.value > r.value:
                    _, current_node, _ = self._left(p, l, r)
                    self._max_heapify(current_node)
                # 右孩子比父亲和左孩子大
                elif r.value > p.value and r.value > l.value:
                    _, _, current_node = self._right(p, l, r)
                    self._max_heapify(current_node)
            # 左孩子比父亲大，没有右孩子
            elif l.value > p.value:
                _, current_node, _ = self._left(p, l, r)
                self._max_heapify(current_node)
        else:
            raise ValueError('method只能取0或1')

    def build_max_heap(self, heap_size=None):
        if heap_size is None:
            heap_size = len(self.nodes)
        for i in range(math.floor(heap_size / 2) - 1, -1, -1):
            self._max_heapify(self.nodes[i], method=0)

    def heap_sort(self):
        heap_size = len(self.nodes)
        while heap_size > 0:
            self.build_max_heap(heap_size=heap_size)
            self.nodes[0].value, self.nodes[heap_size - 1].value = self.nodes[heap_size - 1].value, self.nodes[0].value
            if self.nodes[heap_size - 1] != self.root:
                if self.nodes[heap_size - 1].parent.right is self.nodes[heap_size - 1]:
                    self.nodes[heap_size - 1].parent.right = None
                elif self.nodes[heap_size - 1].parent.left is self.nodes[heap_size - 1]:
                    self.nodes[heap_size - 1].parent.left = None
            yield self.nodes[heap_size - 1].value
            heap_size -= 1


if __name__ == '__main__':
    h = Heap([1, 2, 3, 4, 5, 6, 7])
    for i in h.heap_sort():
        print(i)
    print('-'*10)
    h2 = Heap([7, 6, 5, 4, 3, 2, 1])
    for i in h2.heap_sort():
        print(i)
