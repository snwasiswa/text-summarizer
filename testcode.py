""" The file tests whether the class Summary works as expected"""

import unittest
from textsummary import Summary


class MyTestCase(unittest.TestCase):
    """ Tests for the class Summary"""

    def test_get_summary(self):
        """Test whether the code summarizes input given or not"""

        with open('testfile.txt', 'r') as file:
            data = file.read().replace('\n', '')
            summarize = Summary(data)

        # Test the condition
        self.assertTrue(summarize.get_summary)


if __name__ == '__main__':
    unittest.main()
