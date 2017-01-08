__author__ = 'John'

import unittest

class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def addRear(self, value):
        self.items.insert(0, value)

    def addFront(self, value):
       self.items.append(value)

    def removeRear(self):
        return self.items.pop(0)

    def removeFront(self):
        return self.items.pop()

    def getList(self):
        return self.items

    def size(self):
        return len(self.items)


class Test_Deque(unittest.TestCase):
    def test_isEmpty(self):
        dq = Deque()
        self.assertEqual(dq.isEmpty(), True)

    def test_not_isEmpty(self):
        dq = Deque()
        dq.addRear(4)
        self.assertEqual(dq.isEmpty(), False)

    def test_getList(self):
        dq = Deque()
        self.assertEqual(dq.getList(), [])

    def test_add_front(self):
        dq = Deque()
        dq.addFront('cat')
        dq.addFront(True)
        self.assertEqual(dq.getList(), ['cat', True])

    def test_add_rear(self):
        dq = Deque()
        dq.addRear(4)
        dq.addRear('dog')
        self.assertEqual(dq.getList(), ['dog', 4])

    def test_size(self):
        dq = Deque()
        dq.addFront('cat')
        dq.addFront(True)
        self.assertEqual(dq.size(), 2)

    def test_removeRear(self):
        dq = Deque()
        dq.addFront('cat')
        dq.addFront(True)
        self.assertEqual(dq.removeRear(), 'cat')

    def test_removeFront(self):
        dq = Deque()
        dq.addFront('cat')
        dq.addFront(True)
        self.assertEqual(dq.removeFront(), True)



def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    while chardeque.size() > 1:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            break

    return chardeque.size() <= 1

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))