import matplotlib.pyplot as plt
import numpy as np


class MultiNewton(object):
    def __init__(self, grad_f, hessian_matrix):
        self.grad_f = grad_f
        self.hessian_matrix = hessian_matrix

    def compute_dx(self, bar_x):
        grad = self.grad_f(bar_x)
        hessian_matrix = self.hessian_matrix(bar_x)
        dx = np.linalg.solve(hessian_matrix, - grad)
        return dx

    def solve(self, init_x, n_iter=100):
        self.hist = np.zeros(n_iter)
        bar_x = init_x

        for i in range(n_iter):
            dx = self.compute_dx(bar_x)
            x = bar_x + dx
            print(f"x({i + 1}) = [{x[0]:.2f} {x[1]:.2f}]")
            bar_x = x
            norm_dx = np.linalg.norm(dx)
            self.hist[i] += norm_dx

        return x


if __name__ == "__main__":
    dx0_f = lambda x: 40 * (x[0] ** 3) - 40 * x[0] * x[1] + 2 * x[0] - 2
    dx1_f = lambda x: 20 * x[1] - 20 * (x[0] ** 2)
    grad_f = lambda x: np.array([dx0_f(x), dx1_f(x)])
    hessian_matrix = lambda x: np.array([[120 * (x[0] ** 2) - 40 * x[1] + 2, - 40 * x[0]], [- 40 * x[0], 20 - 40 * x[0]]])

    solver = MultiNewton(grad_f, hessian_matrix)
    res = solver.solve(init_x=np.array([-2, 2]), n_iter=5)
    print(f"Solution is x = [{res[0]:.2f} {res[1]:.2f}]")

    plt.plot(np.arange(0, solver.hist.shape[0]), solver.hist)
    plt.tight_layout()
    plt.savefig('subject6.png')
