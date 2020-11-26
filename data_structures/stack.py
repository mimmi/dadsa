class Stack:

    actual_stack = [None] * 10
    current_index = 0

    def push(self, x):
        self.actual_stack[self.current_index] = x
        self.current_index += 1

    def pop(self):
        top = self.actual_stack[self.current_index - 1]
        self.actual_stack[self.current_index - 1] = None
        self.current_index -= 1
        return top
    
    def display(self):
        return self.actual_stack