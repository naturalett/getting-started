import unittest

# from calculate import calculate
from calculate import calc


class TestCalculator(unittest.TestCase):
    '''Testing the calculator2'''

    def setUp(self):
        '''Set up testing objects'''
        self.a = 200
        self.b = 100

    def test_add(self):
        '''Testing add menthod'''
        calculator = calc.Calc(self.a, self.b)
        print(calculator.add())
        self.assertEqual(calculator.add(), 300)

    def test_is_not_add(self):
        '''Testing add menthod'''
        calculator = calc.Calc(self.a, self.b)
        self.assertNotEqual(calculator.add(), 400)

    def test_sub(self):
        calculator = calc.Calc(self.a, self.b)
        self.assertEqual(calculator.sub(), 100)

    def test_power(self):
        calculator = calc.Calc(self.a, self.b)
        self.assertNotEqual(calculator.power(), 100)

    @unittest.skip
    def test_mul(self):
        calculator = calc.Calc(self.a, self.b)
        self.assertEqual(calculator.mul(), 20000)

    def test_div(self):
        calculator = calc.Calc(self.a, self.b)
        self.assertEqual(calculator.div(), 2)

    def test_mod(self):
        calculator = calc.Calc(self.a, self.b)
        self.assertEqual(calculator.mod(), 0)

    def test_diff_int(self):
        calculator = calc.Calc(self.a, self.b)
        self.assertEqual(calculator.diff_int(), 2)



if __name__ == '__main__':
    unittest.main()

