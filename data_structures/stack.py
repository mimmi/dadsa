class Stack:

    limit = 10
    actual_stack = [None] * limit
    current_index = 0

    # constructor
    def __init__(self, limit):
        self.limit = limit
        self.actual_stack = [None] * limit

    def push(self, x):
        if (self.current_index < self.limit):
            self.actual_stack[self.current_index] = x
            self.current_index += 1
            return True
        else:
            return False

    def pop(self):
        if (self.current_index > 0):
            top = self.actual_stack[self.current_index - 1]
            self.actual_stack[self.current_index - 1] = None
            self.current_index -= 1
            return top
        else:
            return False
    
    def display(self):
        return self.actual_stack