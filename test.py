from data_structures.stack import Stack

# Instantiation
my_stack = Stack(100)

my_stack.push(10)
my_stack.push(10)
my_stack.push(10)
my_stack.push(10)
my_stack.push(10)
my_stack.push(10)
my_stack.push(10)
my_stack.push(10)
my_stack.push(10)
my_stack.push(10)
result = my_stack.push(20)
if (result == False):
    print("Stack is full")

print(my_stack.display())