__author__ = 'John'

import unittest

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


symbs = "{}[]()"
symb_match = {"(": ")", "[": "]", "{" : "}"}

def parChecker(symbolString):
    s = Stack()
    index = 0
    while index < len(symbolString):
        symbol = symbolString[index]
        if symbol in symbs:
            if symbol in symb_match:
                s.push(symbol)
            else:
                if s.isEmpty():
                    break
                else:
                    if not symbol == symb_match[s.pop()]:
                        break
        index = index + 1

    return index == len(symbolString) and s.isEmpty()


class TestParCheck(unittest.TestCase):

    def test_fails(self):
        self.assertFalse(parChecker("("))
        self.assertFalse(parChecker("(*"))
        self.assertFalse(parChecker("( "))
        self.assertFalse(parChecker("[{}()"))
        self.assertFalse(parChecker("[{})"))

    def test_success(self):
        self.assertTrue(parChecker("(5*2) + (3 + 4)"))
        self.assertTrue(parChecker("(5)"))
        self.assertTrue(parChecker("((5))"))
        self.assertTrue(parChecker("[]{}()"))
        self.assertTrue(parChecker("[{}]"))


if __name__ == '__main__':
    unittest.main()
