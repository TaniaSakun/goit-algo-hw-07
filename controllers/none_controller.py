class NoneNode:
    def __init__(self):
        self.height = 0

    def __bool__(self):
        return False

    def __str__(self):
        return ""

    def insert(self, key):
        from controllers.node_controller import Node

        return Node(key)

    def delete(self, key):
        return self

    def sum(self):
        return 0
