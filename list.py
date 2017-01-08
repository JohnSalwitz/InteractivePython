__author__ = 'John'

import unittest

class _ListNode:
    def __init__(self, cargo):
        self.cargo = cargo
        self.next = None
        self.last = None

class List:
    def __init__(self):
        # start of list
        self.head = None
        # end of list
        self.tail = None

    # append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
    def append(self, item):
        node = _ListNode(item)
        if self.tail:
            self.tail.next = node
            node.last = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

    # search(item) searches for the item in the list. It needs the item and returns a boolean value.
    def search(self, item):
        node = self.head
        while node:
            if node.cargo == item:
                return True
            node = node.next
        return False

    # remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
    def remove(self, item):
        node = self.head
        while node:
            if node.cargo == item:
                if node.last:
                    node.last.next = node.next
                else:
                    self.head = node.next

                if node.next:
                    node.next.last = node.last
                else:
                    self.tail = node.last
                break
            node = node.next

    # pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
    def pop(self):
        if self.tail:
            node = self.tail
            if node.last:
                node.last.next = None
                self.tail = node.last
                return node.cargo
            else:
                return None

    # returns the list as a list
    def getList(self):
        lst = []
        node = self.head
        while node:
            lst.append(node.cargo)
            node = node.next
        return lst


class Test_List(unittest.TestCase):

    def test_append(self):
        lst = List()
        lst.append('cat')
        lst.append(True)
        self.assertEqual(lst.getList(), ['cat', True])

    def test_search(self):
        lst = List()
        lst.append(4)
        lst.append('dog')
        self.assertTrue(lst.search('dog'))

    def test_search_fail(self):
        lst = List()
        lst.append(4)
        lst.append('dog')
        self.assertFalse(lst.search('cat'))

    def test_remove(self):
        lst = List()
        lst.append('cat')
        lst.append(True)
        lst.append('dog')
        lst.remove(True)
        self.assertEqual(lst.getList(), ['cat', 'dog'])

    def test_pop(self):
        lst = List()
        lst.append('cat')
        lst.append('dog')
        self.assertEqual(lst.pop(), 'dog')







