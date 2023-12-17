import math
import random

n = int(input("Input number of simulations: "))
radius = 0.25
diameter = radius * 2
square_side = diameter * 2
count = 0
sum_player = 0

for i in range(n):
    sum_player -= 0.25
    center_x, center_y = random.uniform(0, square_side), random.uniform(0, square_side)
    if 0.75 >= center_x >= 0.25 and 0.75 >= center_y >= 0.25:
        count += 1
        sum_player += 1

print("Profit: ", sum_player)
print("Probability: ", count / n * 100, "%")


