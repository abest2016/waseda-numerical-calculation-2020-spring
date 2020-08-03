import numpy as np
import matplotlib.pyplot as plt


def func_dxdt(t, x):
    return - 100 * x


# Euler法（導関数、tの初期値、xの初期値、刻み幅dt）
def euler(func_dxdt, t, x, dt=1e-2):
    x += func_dxdt(t, x) * dt
    t += dt

    return t, x


# 常微分方程式を逐次計算（導関数、xの初期値、tの開始点、tの終了点、刻み幅dx）
def ode_calc(method, func_dxdt, x_start, t_start, t_end, dt=1e-2):
    num_calc = 0  # 計算回数
    t_div = np.abs((t_end - t_start) / dt)  # 格子分割数
    if t_end < t_start:  # 負の方向に計算する時は刻み幅の符号を反転
        dt = -dt

    t_list = [t_start]
    x_list = [x_start]

    while True:
        t, x = method(func_dxdt, t_list[-1], x_list[-1], dt)

        t_list.append(t)
        x_list.append(x)

        num_calc += 1  # 計算回数を数える

        # 「計算回数が格子分割数以上」ならば終了
        if t_div <= num_calc:
            break

    return t_list, x_list


def visualization(x_list, y_list, x_label, y_label):
    plt.xlabel("$" + x_label + "$")
    plt.ylabel("$" + y_label + "$")
    plt.grid()
    plt.plot(x_list, y_list, label="$" + y_label + "$", color='#ff0000')
    plt.legend(loc='best')

    plt.show()


if __name__ == '__main__':

    x_list, y_list = ode_calc(euler, func_dxdt, 1.0, 0.0, 0.1, 1e-6)
    visualization(x_list, y_list, "t", "x(t)")
