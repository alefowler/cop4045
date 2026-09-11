import math
from matplotlib import pyplot as plt


def plot_function(fun_str, domain, ns):
    xmin, xmax = domain
    step = (xmax - xmin) / (ns - 1)
    xs = [xmin + i * step for i in range(ns)]

    ys = []
    for x in xs:
        y = eval(fun_str)
        ys.append(y)

    print("{:.4} {:.4}".format("x", "y"))
    for i in range(len(xs)):
        print("{:.4f} {:.4f}".format(xs[i], ys[i]))

    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    plt.show()


fun_str = input("Enter function with variable x: ")
ns = int(input("Enter number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

plot_function(fun_str, (xmin, xmax), ns)
