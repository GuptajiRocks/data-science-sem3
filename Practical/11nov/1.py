import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def bern():
    p = 0.3

    bernoulli_samples = np.random.binomial(1, p, 1000)

    mean = np.mean(bernoulli_samples)
    median = np.median(bernoulli_samples)
    mode = stats.mode(bernoulli_samples, keepdims=True)[0][0]

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

    plt.hist(bernoulli_samples, bins=[-0.5, 0.5, 1.5], align='mid', rwidth=0.5, color='skyblue', edgecolor='black')
    plt.xlabel('Outcome')
    plt.ylabel('Frequency')
    plt.title('Histogram of Bernoulli Distribution')
    plt.show()

def normal():
    mu = 0
    sigma = 1

    normal_samples = np.random.normal(mu, sigma, 1000)

    mean = np.mean(normal_samples)
    median = np.median(normal_samples)
    mode = stats.mode(normal_samples, keepdims=True)[0][0]

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

    plt.hist(normal_samples, bins=30, color='skyblue', edgecolor='black')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Normal Distribution')
    plt.show()

def die():
    die_rolls = np.random.randint(1, 7, 10000)

    mean = np.mean(die_rolls)
    median = np.median(die_rolls)
    mode = stats.mode(die_rolls, keepdims=True)[0][0]

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)

    outcomes, counts = np.unique(die_rolls, return_counts=True)
    plt.bar(outcomes, counts, color='skyblue', edgecolor='black')
    plt.xlabel('Die Face')
    plt.ylabel('Frequency')
    plt.title('Frequency of Each Outcome in 10,000 Rolls of a Fair 6-Sided Die')
    plt.xticks(outcomes)
    plt.show()

die()