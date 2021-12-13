# basic BST implementation
#


class BST:
    def __init__(self, key):  # creating one root node by default
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
      # checking if root node of object it was called on is empty i.e it has been intialized with None
        if self.key is None:
            self.key = data
            return
            # making greater than or equal to include duplicate vals in left side
        if self.key >= data:
            if self.lchild:  # if left child is present
                self.lchild.insert(data)
                # passig self.lchild is NOT NEEDED !!!because it is called
                # on lchild only it automatically takes the context
            else:  # if no left child is present then we need to insert the data
                self.lchild = BST(data)
        elif self.key < data:
            if self.rchild:
                # if right child is present
                # takes right child context automatically as self as insert is being called on it
                self.rchild.insert(data)
            else:  # if no right child is present we need to insert the data
                # so we need to create a new node
                self.rchild = BST(data)

    def traversal(self):
        # THIS IS INORDER
        if self.key is None:
            print("Root is empty")
        else:
         # in order traversal
            if self.lchild is not None:
                self.lchild.traversal()
            print(self.key, end=" ")
            if self.rchild is not None:
                self.rchild.traversal()
        return

    def search(self, data):

        if self.key == data:
            print("Node found")
        elif self.key >= data:
            if self.lchild:  # if left child exists we will search it
                self.lchild.search(data)
            else:
                print("Node not found")
        elif self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node not found")

    def deletion(self, data, curr):
        if self.key is None:
            print("Tree is empty")
            return

        if data < self.key:
            # to store value after deletion because we need to set child to NONE after deletion
            if self.lchild:
                self.lchild = self.lchild.deletion(data, curr)
            else:
                print("Given Node is Not present in the Tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.deletion(data, curr)
            else:
                print("Given Node is not present in the Tree")
        elif data == self.key:
            # The below two conditions cover also the case of both None since in that case it also has to return NULL
            if self.lchild is None:
                # means right child exists
                # replace the node with its right child
                temp = self.rchild
                if data == curr:  # if its root node we r deleting
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            elif self.rchild is None:
                # replace the node with its left child
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None  # after copying left child val to root node we delete left child
                    return
                self = None
                return temp
            # when node to be deleted has two children
            # either delete the largest key in the left sub tree
            # or smallest key in right subtree which is used here
            node = self.rchild
            while node.lchild:
                node = node.lchild  # reaching the least node in rst since lower val on left
            self.key = node.key  # replacing parent by child node
            # now deleting the child node
            self.rchild = self.rchild.deletion(node.key, curr)

        return self

    '''finding node with min key'''

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
            # even if lchild is not present it will print the root node
        print("node with the smallest key is:", current.key)
       # need this method to delete when only one node is present in the tree

    '''finding node with max key'''

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("node with largest key is:", current.key)


def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)
 # 1 is for root node


global root
root = BST(int(input("Please enter the data for the BST:")))
while(1):
    print("\nEnter your choice:")
    print("\n1. insert\n2. traverse\n3. search\n4. delete \n5. minimum node \n6. maximum node \n7. quit\n")
    ch = int(input())
    if ch == 1:
        root.insert(int(input("Please enter the data to be inserted:")))
    elif ch == 2:
        root.traversal()
    elif ch == 3:
        root.search(int(input("Enter the node to search:")))

    elif ch == 4:
        if count(root) > 1:
            root.deletion(
                int(input("Enter which node you want to delete:")), root.key)
            # 2nd parameter is to check if its root node we are deleting
        else:
            print("Cant perform deletion operation")
    elif ch == 5:
        print(root.min_node())
    elif ch == 6:
        print(root.max_node())
    elif ch == 7:
        quit()
