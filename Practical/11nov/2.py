import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def a():
    p = 0.8

    bernoulli_dist = bernoulli(p)

    x = [0, 1]
    y = bernoulli_dist.pmf(x)

    plt.bar(x, y, color=['skyblue', 'orange'], edgecolor='black', width=0.4)
    plt.xticks(x, ['Failure (0)', 'Success (1)'])
    plt.xlabel('Outcome')
    plt.ylabel('Probability')
    plt.title("PDF of Bernoulli Distribution with p = 0.8")
    plt.show()

def b():
    p = 0.6

    bernoulli_dist = bernoulli(p)

    probability_of_success = bernoulli_dist.pmf(1)

    mean = bernoulli_dist.mean()
    variance = bernoulli_dist.var()

    print("Probability of landing on 6 (success):", probability_of_success)
    print("Mean of the Bernoulli distribution:", mean)
    print("Variance of the Bernoulli distribution:", variance)

a()
