
class Node:
    count = 1
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = Node(value)
                Node.count += 1
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
                Node.count += 1
            else:
                self.right.insert(value)


# Using preorder
def serialize(root, serial):
    if root != None:
        serial.append(root.value)
        serialize(root.left, serial)
        serialize(root.right, serial)
    else:
        serial.append('x')


def deserialize(newRoot, serial):
    if serial[0] == 'x':
        serial.pop(0)
    else:
        if len(serial) > 0:
            newRoot = Node(serial.pop(0))
            print(newRoot.value)
            deserialize(newRoot.left, serial)
            deserialize(newRoot.right, serial)

if __name__ == '__main__':
    print("This program serializes a tree\n")

    root = Node(3)
    root.insert(1)
    root.insert(2)
    root.insert(4)
    root.insert(5)
    root.insert(0)

    # Serialize
    serial = []
    serialize(root, serial)
    print(serial)

    # Deserialize
    newRoot = Node(None)
    deserialize(newRoot, serial)
    print(newRoot.value)