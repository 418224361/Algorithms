class Node:
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class LeftChildRightSibingNode:
    def __init__(self, value=None):
        self.value = value
        self.parent = None
        self.child = None
        self.sibling = None


class BinaryTree:
    def __init__(self, root=None, sub_tree=None):
        if root is None:
            self.root = root
        elif isinstance(root, Node):
            self.root = root
        else:
            raise TypeError('Neither {} is Node type or NIL'.format(root))
        if sub_tree is not None:
            sub_root = sub_tree.root
            if self.root.left is None:
                self.root.left = sub_root
                sub_root.parent = self.root
            elif self.root.right is None:
                self.root.right = sub_root
                sub_root.parent = self.root
            else:
                raise ValueError('Tree is full')

    def isempty(self):
        """
        判断树是否为空
        """
        if self.root is None:
            return True
        return False

    def isleaf(self, node):
        """
        判断node是否是叶子节点
        """
        if node.left is None and node.right is None:
            return True
        return False

    def isroot(self, node):
        """
        判断是否是根节点
        """
        if id(self.root) == id(node):
            return True
        return False

    def add_left(self, pnode, lnode):
        """
        为pnode添加左节点lnode
        """
        if not isinstance(lnode, Node):
            raise TypeError('{} is not Node type'.format(lnode))
        pnode.left = lnode
        lnode.parent = pnode

    def add_right(self, pnode, rnode):
        """
        为pnode添加右节点rnode
        """
        if not isinstance(rnode, Node):
            raise TypeError('{} is not Node type'.format(rnode))
        pnode.right = rnode
        rnode.parent = pnode

    def _search(self, node, root=-1):
        if root == -1:
            root = self.root
        if id(root) == id(node):
            raise StopIteration
        elif self.isleaf(root):
            return False
        else:
            left_subtree_root = root.left
            right_subtree_root = root.right
            if left_subtree_root:
                self._search(node, left_subtree_root)
            if right_subtree_root:
                self._search(node, right_subtree_root)

    def search(self, node):
        """
        在树中查找节点
        """
        try:
            self._search(node)
        except StopIteration:
            return True
        else:
            return False

    def delete(self, node):
        """
        从树中删除节点
        """
        if not self.search(node):
            raise ValueError('not exits')
        if self.isroot(node):
            self.root = None
        else:
            if id(node.parent.left) == id(node):
                node.parent.left = None
            elif id(node.parent.right) == id(node):
                node.parent.right = None

    def walkman(self, node=-1):
        """
        递归打印树的所有节点
        """
        if node == -1:
            node = self.root
        print(node.value)
        left_son = node.left
        right_son = node.right
        if left_son:
            self.walkman(left_son)
        if right_son:
            self.walkman(right_son)

    def walkwoman(self):
        """
        非递归打印树的所有节点
        """
        stack = [self.root]
        while stack:
            node = stack[-1]
            while node:
                node = node.left
                stack.append(node)
            stack.pop()
            if stack:
                node = stack.pop()
                print(node.value)
                node = node.right
                stack.append(node)


class AnyTree:
    def __init__(self, root=None, sub_tree=None):
        if root is None:
            self.root = root
        elif isinstance(root, LeftChildRightSibingNode):
            self.root = root
        else:
            raise TypeError('Neither {} is Node type or NIL'.format(root))
        if sub_tree is not None:
            sub_root = sub_tree.root
            if self.root.left is None:
                self.root.left = sub_root
                sub_root.parent = self.root
            elif self.root.right is None:
                self.root.right = sub_root
                sub_root.parent = self.root
            else:
                raise ValueError('Tree is full')

    def add_child(self, pnode, cnode):
        if isinstance(pnode.child, LeftChildRightSibingNode):  # 如果有左孩子节点
            child_node = pnode.child
            while isinstance(child_node.sibling, LeftChildRightSibingNode):
                child_node = child_node.sibling
            child_node.sibling = cnode
            cnode.parent = pnode
        else:
            pnode.child = cnode
            cnode.parent = pnode


if __name__ == '__main__':
    # 任意树
    lnode1 = LeftChildRightSibingNode(12)
    lnode2 = LeftChildRightSibingNode(15)
    lnode3 = LeftChildRightSibingNode(4)
    lnode4 = LeftChildRightSibingNode(10)
    lnode5 = LeftChildRightSibingNode(2)
    lnode6 = LeftChildRightSibingNode(18)
    lnode7 = LeftChildRightSibingNode(7)
    lnode8 = LeftChildRightSibingNode(14)
    lnode9 = LeftChildRightSibingNode(21)
    lnode10 = LeftChildRightSibingNode(5)

    anytree = AnyTree(lnode6)
    anytree.add_child(lnode6, lnode1)
    anytree.add_child(lnode6, lnode2)
    anytree.add_child(lnode6, lnode3)
    anytree.add_child(lnode2, lnode4)

    # 二叉树
    node1 = Node(12)
    node2 = Node(15)
    node3 = Node(4)
    node4 = Node(10)
    node5 = Node(2)
    node6 = Node(18)
    node7 = Node(7)
    node8 = Node(14)
    node9 = Node(21)
    node10 = Node(5)

    tree = BinaryTree(node6)

    tree.add_left(node6, node1)
    tree.add_right(node6, node4)

    tree.add_left(node1, node7)
    tree.add_right(node1, node3)

    tree.add_left(node4, node5)
    tree.add_right(node4, node9)

    tree.add_left(node3, node10)

    print(tree.search(node1))
    print(tree.search(node2))
    print(tree.search(node3))
    print(tree.search(node4))
    print(tree.search(node5))
    print(tree.search(node6))
    print(tree.search(node7))
    print(tree.search(node8))
    print(tree.search(node9))
    print(tree.search(node10))
    print('\n')
    print(tree.root.value)
    print(tree.root.left.value)
    print(tree.root.left.left.value)
    print(tree.root.left.right.value)
    print(tree.root.left.right.left.value)
    print(tree.root.right.value)
    print(tree.root.right.left.value)
    print(tree.root.right.right.value)

    tree.walkman()
    print('\n')
    tree.walkwoman()
