#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function
and understand its purpose.
Play with it in the Python console to make sure you understand.
"""
import unittest
from parameterized import parameterized
from test_utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    class testaccessnestedmap
    """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        test_access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError),
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """
        function 2
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        if expected_exception is KeyError:
            self.assertEqual(str(context.exception), f"'{path[-1]}' not found in nested map")


if __name__ == '__main__':
    unittest.main()
