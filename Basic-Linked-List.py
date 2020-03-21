class Node:
  def __init__(self, data = None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def add_first(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      current_node = self.head
      self.head = new_node
      self.head.next = current_node


  def add_last(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
    else:
      current_node = self.head
      while current_node.next is not None:
        current_node = current_node.next
      current_node.next = new_node

  def print(self):
    current_node = self.head
    while current_node is not None:
      print(current_node.data)
      current_node = current_node.next

def linked_list_test():
  head_node = Node(15)

  mylinkedlist = LinkedList()
  mylinkedlist.head = head_node
  mylinkedlist.add_last(-9)
  mylinkedlist.add_last(10)
  mylinkedlist.add_first(-3)
  mylinkedlist.add_first(20)

  mylinkedlist.print()

linked_list_test()
