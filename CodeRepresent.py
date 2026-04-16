
import math
# DATA (Real-life example: Monthly expenses of Students)
midpoints = [1500
             , 2500, 3500, 4500, 5500]
#Midpoints represent the mid-value of each class interval (e.g., 1000-2000 => 1500, 2000-3000 => 2500, etc.)
f = [5, 9, 14, 8, 4]
#Frequency (f) represents the number of students in each class interval.
N = sum(f)
#Total number of students (N) is the sum of all frequencies.

# Mean
mean = sum(f[i]*midpoints[i] for i in range(len(f))) / N

# Variance & SD(Measured in the same units as data, useful for understanding data spread)
variance = sum(f[i]*(midpoints[i]-mean)**2 for i in range(len(f))) / N
std_dev = math.sqrt(variance)

# Cumulative frequency(Used for median calculation)
cf = []
total = 0
for freq in f:
    total += freq
    cf.append(total)

# Median
for i in range(len(cf)):
    if cf[i] >= N/2:
        median_class = i
        break
#Lower boundary of median class
L = [1000, 2000, 3000, 4000, 5000][median_class]

#Class width
h = 1000

#cummulative frequency of the class before median class
cf_prev = cf[median_class-1] if median_class > 0 else 0

#Frequency of median class
fm = f[median_class]

#Median Calculation
median = L + ((N/2 - cf_prev) / fm) * h

# Mode calculation
modal_class = f.index(max(f))

# Lower boundary of modal class
L_mode = [1000, 2000, 3000, 4000, 5000][modal_class]

# frequency of modal class and its neighbors
f1 = f[modal_class]  #modal class frequency
f0 = f[modal_class-1] if modal_class > 0 else 0 #previous class frequency
f2 = f[modal_class+1] if modal_class < len(f)-1 else 0 #next class frequency

#(most frequent class) Mode Calculation using formula for grouped data
mode = L_mode + ((f1 - f0) / (2*f1 - f0 - f2)) * h

# GM(Geometric mean) Useful for growth rates, such as population growth or investment returns.
gm = math.exp(sum(f[i]*math.log(midpoints[i]) for i in range(len(f))) / N)

# HM(harmonic mean) Useful for rates and ratios, such as average speed or price per unit.
hm = N / sum(f[i]/midpoints[i] for i in range(len(f)))

#Output Results
print("MONTHLY EXPENSE ANALYSIS")
print("Mean:", round(mean,2))
print("Median:", round(median,2))
print("Mode:", round(mode,2))
print("Geometric Mean:", round(gm,2))
print("Harmonic Mean:", round(hm,2))
print("Variance:", round(variance,2))
print("Standard Deviation:", round(std_dev,2))
