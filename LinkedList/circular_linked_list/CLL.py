# Circular Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node  # point to itself
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")

    def delete(self, data):
        if self.head is None:
            return
        current = self.head
        prev = None
        while True:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    # deleting head node
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = current.next
                    self.head = current.next
                return
            prev = current
            current = current.next
            if current == self.head:
                break


# Example usage
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.display()
cll.delete(2)
cll.display()
