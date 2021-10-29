# Write a function sortStack that receives a stack of integers and returns another stack containing those same integers in sorted order. You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure.

class Stack:
    def __init__(self):
        self.storage = []

    def push(self, item):
        self.storage.append(item)

    def pop(self):
        return self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def is_empty(self): 
        return len(self.storage) == 0

    def print_contents(self):
        for item in self.storage:
            print(item)
      
      
      
def sort_stack(input_stack):
  # init second stack
  output_stack = Stack()
  # loop until the first stack is empty
  # also make sure that we don't leave anything in temp
  temp = None
  while not input_stack.is_empty():
    #  put the top of the first stack in a temp var
    if temp is None:
      temp = input_stack.pop()
    # if the second stack is empty OR temp > the top of the second stack
    if output_stack.is_empty() or temp > output_stack.peek():
      # push temp to the second stack
      output_stack.push(temp)
      temp = None
    # else:
    else:
      # pop the top of the second and push to the first
      input_stack.push(output_stack.pop())
      
  return output_stack
  
s = Stack()
s.push(1)
s.push(10)
s.push(123)
s.push(4)
s.push(55)
s.push(12)
s.push(2)

sorted_stack = sort_stack(s)
sorted_stack.print_contents()