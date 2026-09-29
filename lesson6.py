# import numpy
import numpy as np
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


# Slicing in NumPy array follows the format (start:end:step)
# When omitted (start)defaults to [0], (end) defaults to [the last element] and (step) defaults to 1.
# If (step) is negative, values are retrieved in reverse order.
a = np.array([0,1,2,3,4,5,6,7,8,9,10])
print("When start is omitted:",end = '/t')
print(a[:15:3])
print("When end id omitted:",end= '/t')
print(a[2::3])
print("When step is omitted:", end = '/t')
print(a[2:15:])
print("When step is omitted(2):", end='/t')
print(a[2:15])
print("When step and stop are omitted:",end='/t')
print(a[2:])

# USING NOAA DATA
# We can take the first 7 days and compute the average max temp
tmax_week1 = jan_tmax[0:7]
print("Average TMAX in January week 1:",np.mean(tmax_week1))

# Jan on Fridays
prcp_fri = jan_prcp[::7]
print("January prcp on Fridays:",prcp_fri)

# BOOLEAN INDEXING ->allows user to filter elements of an array based on a condition.
# Uses boolean array to select elements from another array

a = np.array([1,1,2,3,5,8,13])
# Create a list of boolean values
idx = [True,False,False,True,False,True,True]
# Boolean Indexing
print(a[idx])

# We can look at the TMAX and TMIN of days without rain
no_rain = jan_prcp == 0
print("TMAX on days with no rain(first 10):",jan_tmax[no_rain][:10])
print("TMIN on days without rain(first 10):",jan_tmin[no_rain][:10])

# There are extremely large data(999.9) which represents precipitation that was not properly recorded on the last day(missing value)
jan_prcp[:7]
print("Missing value:",jan_prcp)

# When calculating average precipitation we should ignore these data
# This will lead to wrong average
print("Average January PRCP(including missing values):",np.mean(jan_prcp))
jan_prcp_no_missing = jan_prcp[jan_prcp < 999.9]
print("Average January PRCP(excluding missing values):",np.mean(jan_prcp_no_missing))

# We can combine multiple conditions using:
# & -> AND operator
# | -> OR operator
# ~ -> NOT operator

# We can find how many days where TMAX was below -10 degrees AND not rainy.
cold_and_not_rainy = (jan_tmax < -10) & (jan_prcp == 0)
print("Number of days in January that are cold and not rainy:",np.sum(cold_and_not_rainy))
print("January TMAX",jan_tmax)
tmax_mon = jan_tmax[3:31:7]
print("tmax of Mondays:",tmax_mon)