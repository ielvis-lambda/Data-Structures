
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

  def contains(self, target):
        # set a reference to self
        current = self
        while True:
          # Will return False if doesn't contain the item
            if not current:
                return False
          # If there's a match return True
            if current.value == target:
                return True
          # If it's bigger check a node to the left which is lower than current otherwise check right
            elif current.value > target:
                current = current.left
            else:
                current = current.right

  def get_max(self):
      # Set a reference to self
        current = self
        max = 0
        while current:
          # if the current value is greater than the max set it to the current value and move right to check again
            if current.value > max:
                max = current.value
                current = current.right

        return max
