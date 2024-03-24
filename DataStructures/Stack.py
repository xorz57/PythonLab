class Stack:
    def __init__(self):
        self._elements = []

    def __len__(self):
        return len(self._elements)

    def push(self, value):
        self._elements.append(value)

    def pop(self):
        if self._elements:
            return self._elements.pop()
        else:
            return None

    def top(self):
        return self._elements[-1]
