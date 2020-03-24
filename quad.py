import math
import matplotlib.pyplot as plt


def func(a, b, c):

    dsc = pow(b, 2) - (4 * a * c)

    if dsc > 0:
        rt_one = (-b + math.sqrt(dsc)) / (2 * a)
        rt_two = (-b - math.sqrt(dsc)) / (2 * a)

        print(f"Delta is equal to {dsc}")
        print(f"First root is {rt_one} and second root is {rt_two}")

        if rt_one < rt_two:
            x = rt_one
            y = rt_two

        else:
            x = rt_two
            y = rt_one

        roots_one = []
        roots_two = []

        while x < y:
            base = float(a * pow(x, 2) + b * x + c)

            roots_one.append(x)
            roots_two.append(base)
            x += 0.0001

        print(f"Image from roots {roots_one[0]} to {roots_one[-1]} correspond from {roots_two[0]} to {roots_two[-1]}")
        plt.plot(roots_one, roots_two)
        plt.show()

    elif dsc == 0:
        rt_one = (-b + math.sqrt(dsc)) / (2 * a)
        rt_two = (-b - math.sqrt(dsc)) / (2 * a)

        print(f"Delta is equal to {dsc}")
        print(f"First root {rt_one} is equal to second root {rt_two}")

        x = -10

        roots_one = []
        roots_two = []

        while x < 10:
            base = float(a * pow(x, 2) + 2 * x + c)

            roots_one.append(base)
            roots_two.append(x)
            x += 0.0001

        #print(f"Image from roots {roots_one[0]} to {roots_one[-1]} correspond from {roots_two[0]} to {roots_two[-1]}")
        plt.plot(roots_one, roots_two)
        plt.show()

    else:
        print(f"Delta is equal to {dsc}")
        print("Function has no real roots.")


a = 1
b = -5
c = 6

func(a, b, c)
