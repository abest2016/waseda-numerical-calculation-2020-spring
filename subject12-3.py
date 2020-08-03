import numpy as np
import matplotlib.pyplot as plt


def func_dxdt(t, x, y):
    return 0.25 * x - 0.01 * x * y


def func_dydt(t, x, y):
    return - 1.0 * y + 0.01 * x * y


# Euler法（xの導関数、yの導関数、tの初期値、xの初期値、刻み幅dt）
def euler(func_dxdt, func_dydt, t, x, y, dt=1e-2):
    x += func_dxdt(t, x, y) * dt
    y += func_dydt(t, x, y) * dt
    t += dt

    return t, x, y


# 常微分方程式を逐次計算（xの導関数、yの導関数、xの初期値、yの初期値、tの開始点、tの終了点、刻み幅dx）
def ode_calc(method, func_dxdt, func_dydt, x_start, y_start, t_start, t_end, dt=1e-2):
    num_calc = 0  # 計算回数
    t_div = np.abs((t_end - t_start) / dt)  # 格子分割数
    if t_end < t_start:  # 負の方向に計算する時は刻み幅の符号を反転
        dt = -dt

    t_list = [t_start]
    x_list = [x_start]
    y_list = [y_start]

    while True:
        t, x, y = method(func_dxdt,func_dydt, t_list[-1], x_list[-1], y_list[-1], dt)

        t_list.append(t)
        x_list.append(x)
        y_list.append(y)

        num_calc += 1  # 計算回数を数える

        # 「計算回数が格子分割数以上」ならば終了
        if t_div <= num_calc:
            break

    return t_list, x_list, y_list


def visualization(x_list, y_list_1, y_list_2, x_label, y_label, y_list_1_label, y_list_2_label):
    plt.xlabel("$" + x_label + "$")
    plt.ylabel("$" + y_label + "$")
    plt.grid()
    plt.plot(x_list, y_list_1, label="$" + y_list_1_label + "$", color='#ff0000')
    plt.plot(x_list, y_list_2, label="$" + y_list_2_label + "$", color='#2f00ff')
    plt.legend(loc='best')

    plt.show()


if __name__ == '__main__':

    x_list, y_list_1, y_list_2 = ode_calc(euler, func_dxdt, func_dydt, 80, 30, 0, 100, 1e-2)
    visualization(x_list, y_list_1, y_list_2, "t", "Amount", "x(t)", "y(t)")
