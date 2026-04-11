import statistics
import math

# Sample data (you can change values)
data = [10, 20, 20, 30, 40, 50]

print("Data:", data)

# Mean
mean = statistics.mean(data)

# Median
median = statistics.median(data)

# Mode
mode = statistics.mode(data)

# Geometric Mean (GM)
gm = math.prod(data) ** (1/len(data))

# Harmonic Mean (HM)
hm = statistics.harmonic_mean(data)

# Variance
variance = statistics.variance(data)

# Standard Deviation
std_dev = statistics.stdev(data)

# Output
print("\n--- Results ---")
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Geometric Mean =", round(gm, 2))
print("Harmonic Mean =", round(hm, 2))
print("Variance =", variance)
print("Standard Deviation =", round(std_dev, 2))