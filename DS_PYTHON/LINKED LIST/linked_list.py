# singly linked list in python basic operations

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # initialzing empty head for new ll
    def __init__(self):
        self.head = None

    def traversal(self):
        print("\n")
        if self.head == None:
            print("Linked List is empty")
        else:
            cur = self.head
            while cur is not None:
                print(str(cur.data), "->", end="")
                cur = cur.next

    def add_begin(self):

        new_node = Node(int(input("Please enter data of node:")))

        new_node.next = self.head
        self.head = new_node

    def add_end(self):
        new_node = Node(int(input("Please enter data of node:")))
        if self.head is None:  # if LL is empty
            self.head = new_node

        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.next = None

    def add_after(self):
        if self.head is None:
            print("Linked List is empty")

        else:

            val = int(input("Enter the node after which you want to insert"))
            n = self.head
            while n is not None:
                if n.data == val:
                    break
                else:
                    n = n.next
            if n is None:
                print("Item not there in the list")
            else:
                new_node = Node(int(input("Please enter data of the node")))
                new_node.next = n.next
                n.next = new_node

    def add_before(self):
        if self.head is None:
            print("Linked List is empty")
        else:

            val = int(input("Enter the node before which you want to insert:"))
            n = self.head
            if n.data == val:  # if only 1 node in ll
                new_node = Node(
                    int(input("Please enter the data of the node:")))
                new_node.next = n
                self.head = new_node
            else:
                while n.next is not None:
                    if n.next.data == val:
                        break
                    n = n.next
                if n is None:
                    print("Item not there in List")
                else:
                    new_node = Node(
                        int(input("Please enter the data of the node:")))
                    new_node.next = n.next
                    n.next = new_node

    def del_beg(self):
        if self.head is None:
            print("the list is empty!")
        else:
            self.head = self.head.next

    def del_last(self):
        if self.head is None:
            print("The List is empty")
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None

    def del_mid(self):
        if self.head is None:
            print("The list is empty")

        else:
            val = int(input("enter the node to delete:"))
            n = self.head
            if val == n.data:  # if first node is to be deleted
                self.head = n.next
                return
            while n.next is not None:
                if val == n.next.data:
                    break
                n = n.next
            if n.next is None:
                print("Node to be deleted doesnt exist")
            else:
                n.next = n.next.next


LL = LinkedList()
user_continue = True
while user_continue:
    print("\nSelect operation: \n1. Insert at Start\n2. Delete\n3. Traversal \n4. Insert at End\n5. Insert after Node \n6. Insert before Node\n7. Delete first Node \n8. Delete last Node \n9. Delete middle Node \n10. quit:", end="\n")
    user_choice = int(input())
    if user_choice == 1:
        LL.add_begin()
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        LL.traversal()
    elif user_choice == 4:
        LL.add_end()
    elif user_choice == 5:
        LL.add_after()
    elif user_choice == 6:
        LL.add_before()
    elif user_choice == 7:
        LL.del_beg()
    elif user_choice == 8:
        LL.del_last()
    elif user_choice == 9:
        LL.del_mid()
    elif user_choice == 10:
        quit()
