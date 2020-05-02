class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

class Stack:
  def __init__(self):
    self.top = None

  def is_empty(self):
    return self.top is None

  def peek(self):
    return self.top

  def push(self, new_data):
    if self.is_empty():
      self.top = Node(new_data)
    else:
      temp = self.top
      self.top = Node(new_data)
      self.top.next = temp
   
  def pop(self):
    if not self.is_empty():
      self.top = self.top.next
 
  def print(self):
    current_node = self.top
    while current_node is not None:
      print(current_node.data)
      current_node = current_node.next

def stack_test():
  s = Stack()
  s.push(5)
  s.push(10)
  s.pop()
  s.push(41)
  s.pop()
  s.pop()
  s.push(100)
  s.push(3)
  s.print()

stack_test()
