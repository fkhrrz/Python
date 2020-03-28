class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front = None
    self.back = None

  def is_empty(self):
    return self.front is None

  def enqueue(self, new_data):
    new = Node(new_data)
    if self.is_empty():
      self.front = new
    else:
      current = self.front
      while current.next != None:
        current = current.next
      current.next = new
    
  def dequeue(self):
    temp = self.front
    if self.is_empty() is False:
      self.front = self.front.next
    return temp

  def print(self):
    current_node = self.front
    while current_node is not None:
      print(current_node.data)
      current_node = current_node.next

def queue_test():
  q = Queue()
  q.enqueue(5)
  q.enqueue(10)
  q.dequeue()
  q.enqueue(41)
  q.dequeue()
  q.dequeue()
  q.enqueue(100)
  q.enqueue(3)
  q.print()

queue_test()
