class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):  
        self.head = None
  
'''
1st Node = Data: 1, Next: None
second = Data: 2, Next: None
third = Data: 3, Next: None
'''

llist = LinkedList() 

llist.head = Node(100) 
second = Node(200) 
third = Node(300) 

''' 
Three nodes have been created. 
We have references to these three blocks as head, 
second and third 

llist.head        second              third 
     |                |                  | 
     |                |                  | 
+----+------+     +----+------+     +----+------+ 
| 1  | None |     | 2  | None |     |  3 | None | 
+----+------+     +----+------+     +----+------+ 
'''

llist.head.next = second; # Link first node with second  

''' 
Now next of first Node refers to second.  So they 
both are linked. 

llist.head        second              third 
     |                |                  | 
     |                |                  | 
+----+------+     +----+------+     +----+------+ 
| 1  |  o-------->| 2  | null |     |  3 | null | 
+----+------+     +----+------+     +----+------+  
'''

second.next = third; # Link second node with the third node 

''' 
Now next of second Node refers to third.  So all three 
nodes are linked. 

llist.head        second              third 
     |                |                  | 
     |                |                  | 
+----+------+     +----+------+     +----+------+ 
| 1  |  o-------->| 2  |  o-------->|  3 | null | 
+----+------+     +----+------+     +----+------+  
'''

current = llist.head
while (True):
    print(current.data)
    current = current.next
    if (current == None):
        exit()