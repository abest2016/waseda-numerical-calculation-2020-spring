import numpy as np
import matplotlib.pyplot as plt


def func_d2xdt2(t, x):
    return x


# Euler法（導関数、tの初期値、xの初期値、dxdtの初期値、刻み幅dt）
def euler(func_d2xdt2, t, x, dxdt, dt=1e-2):
    x_n = x + dxdt * dt
    dxdt_n = dxdt + func_d2xdt2(t, x) * dt
    t_n = t + dt

    return dxdt_n, t_n, x_n


# 常微分方程式を逐次計算（導関数、dxdtの初期値、xの初期値、tの開始点、tの終了点、刻み幅dx）
def ode_calc(method, func_d2xdt2, dxdt_start, x_start, t_start, t_end, dt=1e-2):
    num_calc = 0  # 計算回数
    t_div = np.abs((t_end - t_start) / dt)  # 格子分割数
    if t_end < t_start:  # 負の方向に計算する時は刻み幅の符号を反転
        dt = -dt

    dxdt_list = [dxdt_start]
    t_list = [t_start]
    x_list = [x_start]

    while True:
        dxdt, t, x = method(func_d2xdt2, t_list[-1], x_list[-1], dxdt_list[-1], dt)

        dxdt_list.append(dxdt)
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

    x_list, y_list = ode_calc(euler, func_d2xdt2, 0, 1.0, 0.0, 1, 0.1)
    visualization(x_list, y_list, "t", "x(t)")
