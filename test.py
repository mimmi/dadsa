import math

stop = 5

def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
       
print(fibonacci(stop))

'''
previous2 = 0
previous1 = 1
print(previous2)
print(previous1)

for i in range(stop):
    current = previous2 + previous1
    previous2 = previous1
    previous1 = current
    print(current)
'''