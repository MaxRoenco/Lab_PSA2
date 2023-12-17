import random

n = int(input("Input number of games: "))
sum_money = 0

for i in range(n):
    count = 0
    x = random.uniform(0, 1)
    y = 0
    while y <= x:
        y = random.uniform(0, 1)
        count += 1
    sum_money += count - 1

print("Average win: ", sum_money / n, "$")
