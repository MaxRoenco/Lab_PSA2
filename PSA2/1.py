from random import randint
import matplotlib.pyplot as plt

n = int(input("How many simulations?"))
data = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0}
for i in range(n):
    dice1, dice2, dice3 = randint(1, 6), randint(1, 6), randint(1, 6)
    sum = dice1 + dice2 + dice3
    if sum in data:
        data[sum] += 1

courses = ["9", "10"]
values = [data[9], data[10]]

fig = plt.figure(figsize=(5, 5))

# creating the bar plot
plt.bar(courses, values, color='maroon', width=0.2)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()