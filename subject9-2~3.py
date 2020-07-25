# Euler法による常微分方程式の解法プログラム
import numpy as np
import matplotlib.pyplot as plt


def func_dydt(x, y):
    return y / (2 * (x + 1))


# Euler法（導関数、xの初期値、yの初期値、刻み幅dx）
def euler(func_dydt, x, y, dx=1e-3):
    dy = func_dydt(x, y) * dx  # 変化量を計算

    x += dx  # 変数を更新
    y += dy  # 変化量を加えて更新

    return x, y


# Heun法（導関数、xの初期値、yの初期値、刻み幅dx）
def heun(func_dydt, x, y, dx=1e-3):

    dy1 = dx * func_dydt(x, y)
    y += (func_dydt(x, y) + func_dydt(x + dx, y + dy1)) * dx / 2
    x += dx

    return x, y


# 4次RungeKutta法（導関数、xの初期値、yの初期値、刻み幅dx）
def rungeKutta(func_dydt, x, y, dx=1e-3):

    dv1 = dx * func_dydt(x, y)
    dv2 = dx * func_dydt(x + dx / 2, y + dv1 / 2)
    dv3 = dx * func_dydt(x + dx / 2, y + dv2 / 2)
    dv4 = dx * func_dydt(x + dx, y + dv3)

    y += (dv1 + 2 * (dv2 + dv3) + dv4) / 6
    x += dx

    return x, y


# 常微分方程式を逐次計算（導関数、yの初期値、tの開始点、tの終了点、刻み幅dt）
def ode_calc(method, func_dydt, y_start, x_start, x_end, dx=1e-2):
    num_calc = 0  # 計算回数
    x_div = np.abs((x_end - x_start) / dx)  # 格子分割数
    if (x_end < x_start):  # 負の方向に計算する時は刻み幅の符号を反転
        dx = -dx

    # 初期値
    x = x_start  # 独立変数t
    y = y_start  # 従属変数y
    print("x = {:.7f},  y = {:.7f}".format(x, y))

    # グラフ用データを追加
    x_list = [x]
    y_list = [y]

    # ずっと繰り返す
    while (True):
        x, y = method(func_dydt, x, y, dx)
        print("x = {:.7f},  y = {:.7f}".format(x, y))

        # グラフ用データを追加
        x_list.append(x)
        y_list.append(y)

        num_calc += 1  # 計算回数を数える

        # 「計算回数が格子分割数以上」ならば終了
        if (x_div <= num_calc):
            print("Finished.")
            print()
            break

    return x_list, y_list


# 可視化
def visualization(x_list, y_list):
    plt.xlabel("$x$")  # x軸の名前
    plt.ylabel("$y(x)$")  # y軸の名前
    plt.grid()  # 点線の目盛りを表示

    plt.plot(x_list, y_list, label="$y(x)$", color='#ff0000')  # 折線グラフで表示
    plt.legend(loc='best')  # 凡例(グラフラベル)を表示
    plt.show()  # グラフを表示


# メイン実行部
if (__name__ == '__main__'):
    # 常微分方程式を逐次計算
    x_list, y_list = ode_calc(euler, func_dydt, 1.0, 0.0, 2.0)

    # 結果を可視化
    visualization(x_list, y_list)

    # 常微分方程式を逐次計算
    x_list, y_list = ode_calc(heun, func_dydt, 1.0, 0.0, 2.0)

    # 結果を可視化
    visualization(x_list, y_list)

    # 常微分方程式を逐次計算
    x_list, y_list = ode_calc(rungeKutta, func_dydt, 1.0, 0.0, 2.0)

    # 結果を可視化
    visualization(x_list, y_list)
