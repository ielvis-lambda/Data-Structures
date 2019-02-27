
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current = self
    complete = False
    while not complete:
      # If the value is less than the current value
      if value < current.value:
        # add value to the left node
        if current.left:
          current = current.left
        else:
          current.left = Node(value)
          complete = True
      # If the value is more than the current value
      if value > current.value:
        # add value to the right node
        if current.right:
          current = current.right
        else:
          current.right = Node(value)
          complete = True

# push test
  def contains(self, target):
    pass

  def get_max(self):
    pass
