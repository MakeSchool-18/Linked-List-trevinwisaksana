class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data: # Check if it already exists
            return False # Prevents adding duplicates
        elif self.value > data: # If a value exists in the data
            if self.leftChild: # If there is a value in the left child
                return self.leftChild.insert(data) # Add the value to the left child
            else: # If there's no value in the left child
                self.leftChild = Node(data) # Create one by using the new data
                return True
        else: # self.value < data
            if self.rightChild: # If there is a value in the right child
                return self.rightChild.insert(data) # Add the new value to the right child
            else: # If there's no value in the right child
                self.rightChild = Node(data) # Create one by using the new data
                return True

    def find(self, data):
        if(self.value is data): # If the current node finds the data that we're looking for
            return True
        elif self.value > data: # If the value is greater than data
            if self.leftChild: # If there is a value in the left child
                return self.leftChild.find(data) # Add the value to the left child
            else: # If there's no value in the left child
                return False # Data doesn't exist
        else: # If the value is smaller than data
            if self.rightChild: # If there is a value in the right child
                return self.rightChild.find(data) # Add the new value to the right child
            else: # If there's no value in the right child
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root: # If the node exists
            return self.root.insert(data)
        else: # If root node does not exists
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root: # If a data exists
            # Return the data
            return self.root.find(data)
        else: # If the data does not exists in the tree
            return False

    def preorder(self):
        print("PreOrder")
        self.root.preorder() # Use the root to call a recursive traversal function

    def postorder(self):
        print("PostOrder")
        self.root.postorder() # Use the root to call

    def inorder(self):
        print("InOrder")
        self.root.inorder() # Use the root to call

def test_binary_tree():
    bst = Tree()
    bst.insert(10)
    print(bst.insert(15))
    bst.preorder()
    bst.postorder()
    bst.inorder()


if __name__ == '__main__':
    test_binary_tree ()
