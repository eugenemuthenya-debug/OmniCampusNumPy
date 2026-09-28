# import numpy
import numpy as np
# Conditional operations
# IN numpy np.ndarray() conditional operations return the result fro each element as np.ndarray,not a universal boolean.
a = np.array([1,2,3,4,5])
b = np.array([2,2,3,6,1])

print("a==a:",a == a)
print("a==b:",a==b)
print("a>b:",a>b)
print("type of a==b:",type(a==b))

URL = "https://www.ncei.noaa.gov/pub/data/cdo/samples/GHCND_sample_csv.csv"
raw = np.loadtxt(URL,delimiter=",",usecols = [6,7,8], skiprows=1)

week_one_tmax = raw[0:7, 0]
week_one_tmin = raw[0:7, 1]
week_one_prcp = raw[0:7, 2]
week_two_tmax = raw[7:14, 0]

week_one_tmax = week_one_tmax/10
week_one_tmin = week_one_tmin/10
week_one_prcp = week_one_prcp/10



# Using NOAA data
print("Week 1 precipitation is zero:",week_one_prcp == 0)
print("Type of boolean array:",type(week_one_prcp))
print("Week 1 MIN less than -10°C:",week_one_tmin < -10)