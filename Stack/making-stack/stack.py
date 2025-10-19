class Stack:
    def __init__(self):
        self.l = []

    def push(self, data):
        self.l.append(data)   # Add to top of stack

    def pop(self):
        if not self.l:
            print("Stack is empty")
            return
        self.l.pop()          # Remove from top (last element)

    def view(self):
        if not self.l:
            print("Stack is empty")
        else:
            print("Top element:", self.l[-1])
