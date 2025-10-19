# Node class to store data and reference to next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List implementation
class LinkedList:
    def __init__(self):
        self.head = None

    # Append a new node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:               # Empty list case
            self.head = new_node
            return

        current = self.head
        while current.next is not None:     # Traverse to the last node
            current = current.next
        current.next = new_node

    # Display the entire linked list
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")                       # Show the end of the list

    # Insert a new node at the beginning
    def start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete the first node
    def del_first(self):
        if self.head is not None:
            self.head = self.head.next

    # Delete the last node
    def del_last(self):
        if self.head is None or self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:  # Stop at second-last node
            current = current.next
        current.next = None

    # Insert a node after a specific value
    def insert_after(self, after, what):
        current = self.head
        while current is not None and current.data != after:
            current = current.next

        if current is None:
            print(f"Value {after} not found.")
            return

        temp = current.next
        current.next = Node(what)
        current.next.next = temp

    # Count total number of nodes
    def count(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        print(f"Total nodes: {count}")

    # Check if a value exists in the list
    def exist(self, val):
        current = self.head
        while current is not None:
            if current.data == val:
                print("True")
                return
            current = current.next
        print("False")


# ---------- Testing the LinkedList ----------
l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.start(0)
l.append(7)
l.append(7)
l.del_first()
l.del_last()
l.insert_after(5, 6)
l.insert_after(2, 3)

l.count()
l.display()
l.exist(0)
