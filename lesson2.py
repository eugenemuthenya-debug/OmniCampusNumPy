# BASIC OPERATIONS
import numpy as np
# We will use data set from NOAA which contains data of daily temperature and precipitation recorded.
# To download and load the dataset as np.array() we will use np.loadtxt().
# This are extra arguments to shape data
# delimiter= "," specify delimiter as a comma
# usecols = [6,7,8] import 7th to 9th column from the csv
# skiprows = 1 do not use the 1st row , it is a header raw
URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv"
raw = np.loadtxt(URL,delimiter=",",usecols = [6,7,8], skiprows=1)

print(raw)

# we slice the data to what we need
week_one_tmax = raw[0:7, 0]
week_one_tmin = raw[0:7, 1]
week_one_prcp = raw[0:7, 2]
week_two_tmax = raw[7:14, 0]
print("Week 1 TMAX",week_one_tmax)
print("Week 1 TMIN",week_one_tmin)
print("Week 1 PRCP",week_one_prcp)

# To check for array size we can us len()
print("Size of week 1 TMAX",len(week_one_tmax))

# We can use .shape(it is mainly common)
print("Size of week 1 TMAX",week_one_tmax.shape)

# MATH OPERATIONS
a = np.array([1,2,3,4,5])
b = np.array([2,2,3,6,1])

print("Sum :",a + b)
# returns the result for each element individually(universal)
print("Difference",a - b)
print("Product", a * b)
print("Quotient", a / b)

# TMAX & TMIN are measured in tenths of degrees(to 1decimal point) we can divide them by 10 to convert.
week_one_tmax = week_one_tmax/10
week_one_tmin = week_one_tmin/10
week_one_prcp = week_one_prcp/10

print("Week 1 TMAX(in celsius):",week_one_tmax)
print("Week 1 TMIN(in celsius):",week_one_tmin)
print("Week 1 PRCP:(in mm)",week_one_prcp)

# we can now calculate metrics such as Daily temp range
week_one_trange = week_one_tmax - week_one_tmin
print("Week 1 TRANGE:", week_one_trange)

# we can also use other python built in functions: .max() and .min() or.sum()
print("Hottest Day in week 1:",np.max(week_one_tmax))
print("Total rainfall in week 1:",np.sum(week_one_prcp))
print("Average TMAX in week 1:",np.mean(week_one_tmax))
print("Standard Deviation of TMAX in week 1:",np.std(week_two_tmax))

# Division by zero
# In python division by zero leads to an error
# a= 2/0
# print(a)

# In numpy it is different
a=np.array([1,2,3])
a / 0
# result should be (inf)infinity

# Other functions
# 1. np.log1p()-computes natural logarithm of one plus the input value. Provides better precisions from smaller values
log_prcp = np.log1p(week_one_prcp)      
print("Log-transformed PRCP:",log_prcp)

# to convert it back np.expm1()
inv_prcp = np.expm1(log_prcp)
print("Inverse log transformed PRCP:",inv_prcp)



