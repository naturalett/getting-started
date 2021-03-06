import unittest
import math

# from calculate import calc
import xmlrunner

from .calc import Calc

class TestCalculator(unittest.TestCase):
    '''Testing the calculator2'''

    def setUp(self):
        '''Set up testing objects'''
        self.a = 200
        self.b = 100

    def test_add(self):
        '''Testing add menthod'''
        calculator = Calc(self.a, self.b)
        print(calculator.add())
        self.assertEqual(calculator.add(), 300)

    def test_subtract(self):
        '''Testing subtract method'''
        calculator = Calc(self.a, self.b)
        self.assertEqual(calculator.sub(), 100)


class PowerTest(unittest.TestCase):
    def test_squares(self):
        for i in range(1, 10):
            self.assertEqual(i * i, math.pow(i, 2))


if __name__ == '__main__':
    with open('results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
    # unittest.main(verbosity=2)


# if __name__ == '__main__':
#     unittest.main()

# python -m xmlrunner