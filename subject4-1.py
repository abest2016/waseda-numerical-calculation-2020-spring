import math


class Function:
    description = 'f(x) = 3 - 4 / (1 + exp(x))'

    def execute(x):
        return 3 - 4 / (1 + pow(math.e, x))


def hit(ans, goal):
    return ans == goal


def solve(l, r, goal, f, method):
    assert method == 'bm' or method == 'fpm'
    assert l < r

    fl = f(l)
    if hit(fl, goal):
        return l

    fr = f(r)
    if hit(fr, goal):
        return r

    if method == 'bm':
        m = (l + r) / 2
    elif method == 'fpm':
        m = l + (r - l) * ((goal - fl) / (fr - fl))

    fl_is_plus = (fl > goal)
    fm_is_plus = (f(m) > goal)
    fr_is_plus = (fr > goal)

    assert fl_is_plus == (not fr_is_plus)

    if fl_is_plus == (not fm_is_plus):
        return solve(l, m, goal, f, method)
    elif fr_is_plus == (not fm_is_plus):
        return solve(m, r, goal, f, method)


if __name__ == '__main__':

    try:
        print('This program solves', Function.description)

        goal = float(input('f(x) should equals to: '))

        print('==========================================')
        print('1 → Bisection Method')
        print('other → False Position Method')
        print('==========================================')
        selection = int(input('Input the number of the method you would like to use: '))

        l = float(input('Input left edge: '))
        r = float(input('Input right edge: '))
        f = Function.execute
        while l >= r or (f(l) > goal) == (f(r) > goal):
            print('Invalid input! Please try again.')
            l = float(input('Input left: '))
            r = float(input('Input right: '))

        if selection == 1:
            print('x =', solve(l, r, goal, f, 'bm'))
        else:
            print('x =', solve(l, r, goal, f, 'fpm'))
    except ValueError:
        print('Not a number.')
