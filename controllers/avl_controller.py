from controllers.none_controller import NoneNode


class Avl:
    def __init__(self):
        self.root = NoneNode()

    def __str__(self):
        return self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if not node:
            return ""
        left_str = self.traverse_in_order(node.left)
        right_str = self.traverse_in_order(node.right)
        return f"{left_str} {node.key} {right_str}"

    def insert(self, key):
        self.root = self.root.insert(key)

    def insert_many(self, keys):
        for key in keys:
            self.insert(key)

    def delete(self, key):
        self.root = self.root.delete(key)

    def delete_many(self, keys):
        for key in keys:
            self.delete(key)

    def min_key(self):
        return self.root.get_min_node().key if self.root else None

    def max_key(self):
        return self.root.get_max_node().key if self.root else None

    def total_sum(self):
        return self.root.sum() if self.root else 0
