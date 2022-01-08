class Calc:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

    def power(self):
        return self.a ** self.b

    def div(self):
        return self.a / self.b

    def sub(self):
        return self.a - self.b

    def diff_int(self):
        return self.a // self.b

    def mod(self):
        return self.a % self.b


def main():
    a = 2
    b = 4
    calculator = Calc(a, b)
    print(str(a) + '+' + str(b) + ' =', calculator.add())
    print(str(a) + '-' + str(b) + ' =', calculator.sub())
    print(str(a) + '*' + str(b) + ' =', calculator.mul())
    print(str(a) + '/' + str(b) + ' =', calculator.div())
    print(str(a) + '/' + str(b) + ' =', calculator.diff_int())
    print(str(a) + '/' + str(b) + ' =', calculator.mod())
    print(str(a) + '/' + str(b) + ' =', calculator.power())


if __name__ == '__main__':
    main()
