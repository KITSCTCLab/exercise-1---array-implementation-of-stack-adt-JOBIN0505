import os
class Stack:
   def _init_(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
         if len(self.items) == 0:
            return True


    def is_full(self):
        if len(self.items) >= size:
            return True

    def push(self, data):
       if not self.is_full():
            # Write code here
            self.items.append(data)
            
        else:
            self.top=self.top+1
            self.stack[self.top]=int(input('enter the data:'))
            print(self.stack)
    def pop(self):
        if not self.is_empty():
            x = self.items.pop()
            return x
        else:
            self.stack[self.top]=None
            self.top=self.top-1
            print(self.stack)
    def status(self):
       for item in self.items:
            print(item)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
