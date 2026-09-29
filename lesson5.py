# import numpy
import numpy as np
# Numpy Indexing 1(1D arrays)
URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv"
raw = np.loadtxt(URL,delimiter=",",usecols = [6,7,8], skiprows=1)

week_one_tmax = raw[0:7, 0]
week_one_tmin = raw[0:7, 1]
week_one_prcp = raw[0:7, 2]
week_two_tmax = raw[7:14, 0]

week_one_tmax = week_one_tmax/10
week_one_tmin = week_one_tmin/10
week_one_prcp = week_one_prcp/10

jan_tmax = raw[0:31, 0]
jan_tmin = raw[0:31, 1]
jan_prcp = raw[0:31, 2]

# convert them to their respective units
jan_tmax = jan_tmax/10
jan_tmin = jan_tmin/10
jan_prcp = jan_prcp/10

# We can retrieve values of NumPy's !D arrays at any position using []
# Use of negative indices corresponds to counting from the end of the array.
# Indexing starts from 0
# INdexing from the back starts from -1
a = np.array([1,2,3,4,5])
print(a[0])
print(a[1])
print(a[-1])
print(a[-2])

# we can find the max temp on the first day of recording
print("First day of January TMAX:",jan_tmax[0])

# Data at the end of January
print("Last day of January TMAX:",jan_tmax[-1])
print("Last day of January TMIN:",jan_tmin[-1])
print("LAST DAY OF JANUARY PRCP:",jan_prcp[-1])

# You can as well specify multiple indices as a list to retrieve multiple values
print("January TMAX every week(in order):",jan_tmax[[0,7,14,21,28]])
print("January TMAX every week(in random order):",jan_tmax[[7,0,14,28,21]])

