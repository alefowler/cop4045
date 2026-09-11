import math
import numpy as np  
from matplotlib import pyplot as plt

while True:
    user_input= input("Enter a (Enter to exit): ")
    if user_input == '':
          break

    a = float(user_input)
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
 
 # discriminant = b^2 - 4ac
    d = (b**2) - (4*a*c)

    if d > 0:
            x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
            x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
            print(f"two solutions: x1={x1:.5f} and x2={x2:.5f}")
    elif d == 0:
            x = -b / (2*a)
            print(f"one solution: {x:.5f}")
    else:
            print("no real solutions")

# plotting quadratic function
    x = np.linspace(-10, 10, 150)
    y = a*x**2 + b*x + c

    plt.plot(x, y)
    plt.title(f'Quadratic Function: {a}x^2 + {b}x + {c}')
    plt.show()

