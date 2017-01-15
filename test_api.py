import unittest
from controllers import Controllers


class MyTestCase(unittest.TestCase):
    def test_luz(self):
        c = Controllers()
        negocio = c.managerluz(0)
        self.assertEquals(negocio, 'desligar')


if __name__ == '__main__':
    unittest.main()
