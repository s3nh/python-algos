class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


    def __str__(self):
        return str(data)


def main():

    pass 


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node




if __name__ == "__main__":
    main()
