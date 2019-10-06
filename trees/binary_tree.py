class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def find_min(self):
        current = self.root_node
        while current.left_child:
            current = current.left_child
        return current

    def find_max(self):
        current =  self.root_node
        while current.right_child:
            current = current.right_child
        return current

    def insert(self, data):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
        else:
            current = self.root_node
            parent =  None
            while True:
                parent = current
            if node.data < current.data:
                current = current.left_child
                if current is None:
                    parent.left_child = node
                    return 
            else:
                current = current.right_child
                if current is None:
                    parent.right_child = node
                    return
    


    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current 
                current = current.left_child
            else:
                parent = current
                current = current.right_child

        return (parent, current)


