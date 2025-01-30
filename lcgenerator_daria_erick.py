import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# (0, 1] Does not include 0
def lcg(seed, a=1664525, c=1013904223, m=2**32, n=1000000):
    random_numbers = []
    for _ in range(n):
        seed = (a * seed + c) % m
        value = (seed / m)  # Normal (0,1)
        value = max(value, 1e-10)  #Avoiding 0
        random_numbers.append(value)
    return random_numbers

#  [1,100]
def lcg_scaled(seed, n=1000000, low=1, high=100):
    numbers = lcg(seed, n=n)  # Obtener números en (0,1]
    scaled_numbers = [low + (high - low) * num for num in numbers]
    return scaled_numbers

# Generate
seed = 42
numbers_01 = lcg(seed, n=9000000)  # (0,1]
numbers_100 = lcg_scaled(seed, n=9000000, low=1, high=100)  # [1,100]

# Seaborn (this just makes the graph prettier)
sns.set_style("whitegrid")

# Dsitributions (0,1]
plt.figure(figsize=(12, 5))
sns.histplot(numbers_01, bins=50, kde=True, color="royalblue", edgecolor='gray', alpha=0.7)
sns.kdeplot(numbers_01, color="black", linewidth=2) #Soft line distro 
plt.title("Distribution (0,1]", fontsize=14)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.show()

# [1,100]
plt.figure(figsize=(12, 5))
sns.histplot(numbers_100, bins=50, kde=True, color="olivedrab", edgecolor='gray', alpha=0.7)
sns.kdeplot(numbers_01, color="black", linewidth=2)  
plt.title("Distribution [1,100]", fontsize=14)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.show()

