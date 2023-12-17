import random
import matplotlib.pyplot as plt


def toss_coin(num_tosses):
    return sum(random.randint(0, 1) for _ in range(num_tosses))


def simulate_experiment(num_experiments, num_tosses):
    results = [toss_coin(num_tosses) for _ in range(num_experiments)]
    return results


def plot_experiment_results(results):
    frequency = {}
    for result in results:
        if result in frequency:
            frequency[result] += 1
        else:
            frequency[result] = 1

    n_values = list(range(35, 66))
    proportion = [frequency.get(n, 0) / len(results) for n in n_values]

    plt.bar(n_values, proportion, width=0.5)
    plt.xlabel('Number of Heads')
    plt.ylabel('Proportion of Experiments')
    plt.title('Proportion of Experiments vs Number of Heads')
    plt.show()


num_experiments = 1000
num_tosses = 100

results = simulate_experiment(num_experiments, num_tosses)

plot_experiment_results(results)
print("Yes")
