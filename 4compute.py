import numpy as np 
import statistics as stats

data = ([10,20,30,40,50,20])
mean=np.mean(data)
median = np.median(data)
mode=stats.mode(data)

var=np.var(data)
std=np.std(data)

print(mean, median, mode, var, std)