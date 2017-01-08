__author__ = 'John'

import unittest

class BTree():
    def __init__(self, tdef):
        self.tree_def = tdef

    def get_min_depth(self):
        return self.min_depth(1)

    def min_depth(self, t_node_inx):

        t_node = self.tree_def[t_node_inx-1]

        if t_node[0] == 0 and t_node[1] == 0:
            return 1

        # left
        if t_node[1] == 0:
            return self.min_depth(t_node[0]) + 1

        # right
        if t_node[0] == 0:
            return self.min_depth(t_node[1]) + 1

        return min(self.min_depth(t_node[0]), self.min_depth(t_node[1])) + 1


tree1_def = [
            (2,3),      # 1
            (4,5),      # 2
            (0,0),      # 3
            (0,0),      # 4
            (0,0)]      # 5

tree2_def = [
            (2,3),      # 1
            (4,5),      # 2
            (0,6),      # 3
            (0,0),      # 4
            (0,0),      # 5
            (0,7),      # 6
            (0,0)]      # 7

class TreeCheck(unittest.TestCase):

    def test_depth(self):
        self.assertEqual(BTree(tree1_def).get_min_depth(), 2)
        self.assertEqual(BTree(tree2_def).get_min_depth(), 3)
