class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root:
                print(root.value)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self._root)

    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root:
                _in_order_traversal(root.left)
                print(root.value)
                _in_order_traversal(root.right)
        _in_order_traversal(self._root)

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.value)
        _post_order_traversal(self._root)

    def contains(self, value):
        def _contains(root, value):
            if root is None:
                return False
            elif value < root.value:
                return _contains(root.left, value)
            elif value > root.value:
                return _contains(root.right, value)
            else:
                return True
        return _contains(self._root, value)

    def insert(self, value):
        def _insert(root, value):
            if root is None:
                return BinarySearchTreeNode(value)
            elif value < root.value:
                root.left = _insert(root.left, value)
            elif value > root.value:
                root.right = _insert(root.right, value)
            else:
                return None
            return root
        self._root = _insert(self._root, value)
        if self._root:
            self._size += 1
