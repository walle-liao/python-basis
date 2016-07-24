import unittest

from lesson1.demo1 import sigmod


class MyTestCase(unittest.TestCase):

    def test_sig(self):
        y = sigmod(0)
        self.assertEquals(y, 0.5, 'input 0, output is 0.5')


if __name__ == '__main__':
    unittest.main()
