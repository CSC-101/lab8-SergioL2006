import unittest

import group


class Lab8_test(unittest.TestCase):

    def test_group_1(self):
        result = group.groups_of_3([1,2,3,5,6,7])
        check = [[1,2,3],[5,6,7]]
        self.assertEqual(check, result)

    def test_group_2(self):
        result = group.groups_of_3([1,2,3,4,5])
        check = [[1,2,3],[4,5]]
        self.assertEqual(check, result)

    def test_group_3(self):
        result = group.groups_of_3([1,2,3,4])
        check = [[1,2,3], [4]]
        self.assertEqual(check, result)

    def test_group_4(self):
        result = group.groups_of_3([1,2])
        check = [[1,2]]
        self.assertEqual(check, result)

    def test_group_5(self):
        result = group.groups_of_3([1])
        check = [[1]]
        self.assertEqual(check, result)