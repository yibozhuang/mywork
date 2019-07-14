class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def push(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node

  def printList(self):
    temp = self.head
    while(temp):
      print temp.data
      temp = temp.next

  def addTwoLists(self, first, second):
    prev = None
    temp = None
    carry = 0

    while (first is not None or second is not None):
      if (first is None):
        data1 = 0
      else:
        data1 = first.data

      if (second is None):
        data2 = 0
      else:
        data2 = second.data

      sum = carry + data1 + data2

      if (sum >= 10):
         sum = sum % 10
         carry = 1
      else:
         carry = 0

      temp = Node(sum)
      if self.head is None:
        self.head = temp
      else:
        prev.next = temp

      prev = temp
      if first is not None:
        first = first.next
      if second is not None:
        second = second.next

    if carry > 0:
      temp.next = Node(carry)


def reverseList(original_list):
  reversed = LinkedList()
  iterator = original_list.head
  while (iterator is not None):
    reversed.push(iterator.data)
    iterator = iterator.next
  return reversed


testReverse = LinkedList()
testReverse.push(1)
testReverse.push(6)
testReverse.push(9)
testReverse.push(3)

print "Before:"
testReverse.printList()

reversed = reverseList(testReverse)

print "After:"
reversed.printList()



first = LinkedList()
second = LinkedList()

first.push(0)
first.push(5)
first.push(2)
first.push(2)

print "First list:"
first.printList()

second.push(0)
second.push(9)
second.push(1)
second.push(0)

print "Second List:"
second.printList()

firstReverse = reverseList(first)
secondReverse = reverseList(second)


res = LinkedList()
res.addTwoLists(first.head, second.head)
resReverse = reverseList(res)

print "Result:"
resReverse.printList()


