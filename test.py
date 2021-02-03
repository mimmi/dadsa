# Queue
from data_structures.queue import Queue

my_queue = Queue(5)

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

my_queue.display()
print("-- printing done --")
my_queue.dequeue()
print("-- dequeue done --")
my_queue.display()
print("-- printing done --")
my_queue.dequeue()
print("-- dequeue done --")
my_queue.display()
print("-- printing done --")