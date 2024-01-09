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
    def test_access_nested_map(self, nested_map, path, result):
        """
        test_access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a KeyError is raised properly."""
        try:
            access_nested_map(nested_map, path)
        except KeyError as error:
            self.assertEqual(str(error), path[-1])
        else:
            self.fail("Expected KeyError but no exception was raised.")


if __name__ == '__main__':
    unittest.main()
