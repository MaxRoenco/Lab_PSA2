import random

n = int(input("Input number of simulations: "))
num = int(input("Input number of participants: "))
lose = 0

for i in range(n):
    close = False
    seats = list(range(num))
    random.shuffle(seats)

    for j in range(num):
        if seats[j] == seats[(j+1) % num] + 1 or seats[j] == seats[(j+1) % num] - 1 or seats[j] == num - 1 and seats[(j+1) % num] == 0:
            lose += 1
            break


print("Probability that two people will sit next to each other is:", (lose / n), "%")
