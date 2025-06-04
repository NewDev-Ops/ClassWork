from turtledemo.penrose import start


class treenode:
    def __init__(self, data):
        self._left = None
        self._right = None
        self._data = data

    def insert_value(self, data):
        if data < self._data:
            if self._left is None:
                self._left = treenode(data)
            else:
                self._left.insert_value(data)

        elif data > self._data:
            if self._right is None:
                self._right = treenode(data)
            else:
                self._right.insert_value(data)


    def find_value(self, data):
        if data < self._data:
            if self._left is None:
                return False
            else:
                return self._left.find_value(data)

        elif data > self._data:
            if self._right is None:
                return False
            else:
                return self._right.find_value(data)

        else:
            return True

    def remove_value(self, data):
        pass

    def preorder_traversal(self):

        print(self._data, end=",")

        if self._left:
            self._left.preorder_traversal()

        if self._right:
            self._right.preorder_traversal()


    def postorder_traversal(self):

        if self._left:
            self._left.postorder_traversal()

        if self._right:
            self._right.postorder_traversal()

        print(self._data, end=",")

    def inorder_traversal(self):

        if self._left: # Returns 2 values, True or False. If it has a value = True, if it has nothing = false
            self._left.inorder_traversal()

        print(self._data, end=",")

        if self._right:
            self._right.inorder_traversal()



if __name__ == '__main__':
    Tree = treenode(50)
    Tree.insert_value(11)
    Tree.insert_value(12)
    Tree.insert_value(13)
    Tree.insert_value(14)
    Tree.insert_value(72)
    Tree.insert_value(62)
    Tree.insert_value(51)
    Tree.insert_value(67)
    Tree.insert_value(82)

    print("")
    print("Inorder Traversal")
    Tree.inorder_traversal()

    print("")
    print("Preorder Traversal")
    Tree.preorder_traversal()

    print("")
    print("Find the value")
    print(Tree.find_value(9))

