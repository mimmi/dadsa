# enqueue <- push something into the queue
# dequeue <- remove the oldest/first item in the queue

class Queue:

    limit = 10
    actual_queue = [None] * limit
    start = 0
    current_index = 0

    def __init__(self, limit):
        self.limit = limit
        self.actual_queue = [None] * limit
    def enqueue(self, x):
        self.actual_queue[self.current_index] = x
        self.current_index += 1
    def display(self):
        for y in self.actual_queue:
            if y != None:
                print(y)
    def dequeue(self):
        print(self.actual_queue[self.start])
        self.actual_queue[self.start] = None
        self.start += 1