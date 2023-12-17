import random

n = int(input("Input number of executions: "))
child1_total = 0
child2_total = 0

for i in range(n):
    child1 = 0
    child2 = 0
    has_boy1 = False
    while not has_boy1:
        child1 += 1
        if random.randint(0, 1) == 1:
            has_boy1 = True

    has_boy2 = False
    has_girl2 = False
    while not (has_boy2 and has_girl2):
        child2 += 1
        if random.randint(0, 1) == 1:
            has_boy2 = True
        else:
            has_girl2 = True

    child1_total += child1
    child2_total += child2

avg_child1 = child1_total / n
avg_child2 = child2_total / n
difference = child2_total - child1_total

print("Average number of children until one boy:", avg_child1)
print("Average number of children until at least one boy and one girl:", avg_child2)
print("Difference in the number of children between scenarios:", difference)
