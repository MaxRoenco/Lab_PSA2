import random

time = 2 * 365
sum_money = 0
count = 0

for i in range(time):
    chance_caught = random.randint(1, 100)
    chance_taxatoare = random.randint(1, 100)
    if chance_taxatoare <= 2:
        sum_money -= 6
    elif chance_caught <= 5:
        if count == 0:
            sum_money -= 50
        elif count == 1:
            sum_money -= 200
        else:
            sum_money -= 300
        count += 1
print(time)
print("Sum of penalty: ", sum_money, "lei")
print("Average per one trip: ", sum_money / time, "lei")
