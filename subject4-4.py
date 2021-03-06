import math


class Function:
    description = 'f(x) = 3 - 4 / (1 + exp(x))'

    def execute(x):
        return 3 - 4 / (1 + pow(math.e, x))

    def execute_derivative(x):
        return 4 * pow(math.e, x) / pow((pow(math.e, x) + 1), 2)


def hit(ans, goal):
    return abs(ans - goal) < 0.0001


def solve(init, f, df, resistance):
    current = init
    while True:
        prev = current
        try:
            current = prev - resistance * f(prev) / df(prev)
        except ZeroDivisionError:
            return 'Failed!'
        if hit(current, prev):
            break
    return current


if __name__ == '__main__':

    try:
        print('This program solves', Function.description, " by Newton's method")

        x0 = float(input('Initial value: '))
        resistance = float(input('Resistance: '))

        print('x =', solve(x0, Function.execute, Function.execute_derivative, resistance))
    except ValueError:
        print('Not a number.')