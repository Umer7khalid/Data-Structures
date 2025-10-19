class Stack:
    def __init__(self):
        self.l = []

    def push(self, data):
        self.l.append(data)

    def pop(self):
        if not self.l:
            return
        self.l.pop()

    def view(self):
        if not self.l:
            return False
        return self.l[-1]


class BracketChecker:
    def bracket(self, string):
        a = Stack()

        for i in string:
            if i in "{[(":
                a.push(i)
            elif i in "}])":
                if i == ')' and a.view() == '(':
                    a.pop()
                elif i == '}' and a.view() == '{':
                    a.pop()
                elif i == ']' and a.view() == '[':
                    a.pop()
                else:
                    return False
            else:
                continue

        return not a.view()  # True if stack is empty


# Example
checker = BracketChecker()
print(checker.bracket("(({}()))"))  # ✅ True
print(checker.bracket("(({}()]"))   # ❌ False
