from controllers.none_controller import NoneNode


class Node:
    def __init__(self, key=None):
        self.key = key
        self.height = 1
        self.left = NoneNode()
        self.right = NoneNode()

    def __bool__(self):
        return self.height != 0

    def get_balance(self):
        return self.left.height - self.right.height

    def update_height(self):
        self.height = 1 + max(self.left.height, self.right.height)

    def left_rotate(self):
        new_node = self.right
        new_node.left, self.right = self, new_node.left
        self.update_height()
        new_node.update_height()
        return new_node

    def right_rotate(self):
        new_node = self.left
        new_node.right, self.left = self, new_node.right
        self.update_height()
        new_node.update_height()
        return new_node

    def get_min_node(self):
        return self.left.get_min_node() if self.left else self

    def get_max_node(self):
        return self.right.get_max_node() if self.right else self

    def insert(self, key):
        if key < self.key:
            self.left = self.left.insert(key)
        elif key > self.key:
            self.right = self.right.insert(key)
        else:
            return self
        self.update_height()
        balance = self.get_balance()
        if balance > 1:
            if key < self.left.key:
                return self.right_rotate()
            else:
                self.left = self.left.left_rotate()
                return self.right_rotate()
        elif balance < -1:
            if key > self.right.key:
                return self.left_rotate()
            else:
                self.right = self.right.right_rotate()
                return self.left_rotate()
        return self

    def sum(self):
        return self.key + self.left.sum() + self.right.sum()

    def delete(self, key):
        if key < self.key:
            self.left = self.left.delete(key)
        elif key > self.key:
            self.right = self.right.delete(key)
        else:
            if not self.left:
                return self.right
            elif not self.right:
                return self.left
            temp = self.right.get_min_node()
            self.key = temp.key
            self.right = self.right.delete(temp.key)
        if not self:
            return self
        self.update_height()
        balance = self.get_balance()

        if balance > 1:
            if self.left.get_balance() >= 0:
                return self.right_rotate()
            else:
                self.left = self.left.left_rotate()
                return self.right_rotate()
        elif balance < -1:
            if self.right.get_balance() <= 0:
                return self.left_rotate()
            else:
                self.right = self.right.right_rotate()
                return self.left_rotate()
        return self
