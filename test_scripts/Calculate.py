import math


class Calculate(object):
    def add(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            return "除数不能为0"
        except TypeError:
            return "类型错误"
        else:
            return result


if __name__ == '__main__':
    c = Calculate()
    print(c.divide(1, 'a'))
