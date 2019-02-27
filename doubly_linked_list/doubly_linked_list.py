"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    current_head = self.head
    # If there is no head create a new ListNode and set the head and the tail to this new node.
    if not current_head:
      node = ListNode(value)
      self.head = node
      self.tail = node
    # If there is a head then we can add this head value before our current value and point back to it using head.prev
    else:
      current_head.insert_before(value)
      self.head = current_head.prev
    return self.head

  def remove_from_head(self):
    current_head = self.head
    # If there is no head return None
    if not current_head:
      return None
    # If there are one or more elements
    else:
      current_head.delete()
      return current_head.value


  def add_to_tail(self, value):
    current_tail = self.tail
    # If there is no element make it the current tail
    if not current_tail:
      node = ListNode(value)
      self.head = node
      self.tail = node
    # If there is one or more element insert after the current tail and set the new tail to be this value's `next`
    else:
      current_tail.insert(value)
      self.tail = current_tail.next
    pass

  def remove_from_tail(self):
    self.tail.delete()
    pass

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass
