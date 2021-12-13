class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Doubly_LL:
    def __init__(self):
        self.head = None

    def add_at_beg(self):
        new_node = Node(int(input("Please enter data for the node:")))
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_at_end(self):
        new_node = Node(int(input("Please enter data for the node:")))
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def insert_before(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            val = int(
                input(("Enter the node before which you want to insert new node:")))
            cur = self.head
            if cur.data == val:
                new_node = Node(int(input("Please enter the node data:")))
                new_node.next = cur
                cur.prev = new_node
                self.head = new_node
            else:
                while cur is not None:
                    if cur.next.data == val:
                        break
                    cur = cur.next
                if cur is None:
                    print("Node doesnt exist")
                else:
                    new_node = Node(
                        int(input("Please enter the data of the node:")))

                    cur.next.prev = new_node
                    new_node.next = cur.next
                    cur.next = new_node
                    new_node.prev = cur

    def insert_after(self):
        if self.head is None:
            print("The list is empty")
        else:

            cur = self.head
            val = int(
                input("Please enter the node after which you want to insert:"))
            while cur is not None:
                if cur.data == val:
                    break
                cur = cur.next
            if cur is None:
                print("The node doesnt exist")

            else:
                new_node = Node(
                    int(input("Please enter the data of the node:")))
                new_node.next = cur.next
                if cur.next is not None:
                    cur.next.prev = new_node
                # for inserting at end we don't need a back reference
                cur.next = new_node
                new_node.prev = cur

    def traversal(self):

        if self.head is None:
            print("Linked List is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, "->", end="")
                cur = cur.next

    def traversal_reversal(self):
        if self.head is None:
            print("The Linked List is empty")
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            while cur is not None:
                print(cur.data, "->", end="")
                cur = cur.prev

    def delete_beg(self):
        if self.head is None:
            print("The Linked List is empty")

        else:
            if self.head.next is None:
                self.head = None
                print("DLL now empty")
            else:
                self.head = self.head.next
                self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("The Linked List is empty")
        if self.head.next is None:
            self.head = None
            print("DLL is empty after del")
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.prev.next = None


user_continue = True
dll = Doubly_LL()
while user_continue:
    print("\nEnter your choice \n1. insert at beginning \n2. insert at end \n3. Insert before \n4. Insert after\n5. delete first node \n6. Delete last node \n7. Traversal \n8. Reverse Traversal \n9. quit")
    user_choice = int(input("Enter the choice:"))
    if user_choice == 1:
        dll.add_at_beg()
    elif user_choice == 2:
        dll.add_at_end()
    elif user_choice == 3:
        dll.insert_before()
    elif user_choice == 4:
        dll.insert_after()
    elif user_choice == 5:
        dll.delete_beg()
    elif user_choice == 6:
        dll.delete_end()
    elif user_choice == 7:
        dll.traversal()
    elif user_choice == 8:
        dll.traversal_reversal()
    elif user_choice == 9:
        quit()
    else:
        print("Please enter a valid operation")
