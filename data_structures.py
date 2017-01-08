__author__ = 'John'

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


def revstring(str):
    str_stack = Stack()
    for chr in str:
        str_stack.push(chr)

    back_str = []
    while(not str_stack.isEmpty()):
        back_str.append(str_stack.pop())

    return "".join(back_str)


print(revstring("hi there"))

