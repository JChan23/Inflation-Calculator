import matplotlib.pyplot as plt
import numpy as np

#Inital amount of money must be a numeric value
valid = False
while valid == False:
    try:
        nominal = float(input("Enter initial value/amount money in $: "))
        nominal = round(nominal, 2)
        valid = True
    except ValueError:
        print("Please enter a numeric value \n")

#year must be a numeric value
valid = False
while valid == False:
    try:
        start = int(input("Enter start year: "))
        valid = True
    except ValueError:
        print("Start year must be a numeric value \n")

#year must be a numeric value
#end year must be greater than start year
YearCheck = False
while YearCheck == False:
    valid = False
    while valid == False:
        try:
            end = int(input("Enter end year: "))
            valid = True
        except ValueError:
            print("End year must be a numeric value \n")
    if start >= end:
        print("End year must be greater than start year \n")
    else:
        YearCheck = True

#rate of inflation/deflation must be a numeric value
valid = False
while valid == False:
    try:
        rate = float(input("Enter rate of inflation (%), or a negative value for deflation (%): "))
        valid = True
    except ValueError:
        print("Inflation/deflation must be a numeric value \n")

#calculations for output and graphing
real = round((nominal/(1+(rate/100))**(end-start)), 2) #final value
real_values = []
real_values.append(nominal)
count = end-start
depreciating_asset = nominal
for i in range(count):
    depreciating_asset = round(depreciating_asset/(1+(rate/100)), 2)
    real_values.append(depreciating_asset)

#different outputs depending on whether it was inflation or deflation
if rate >= 0:
    print(f"\nReal value of ${nominal} after accounting for {end-start} years of inflation at a rate of {rate}% per annum is ${real}")
else:
    print(f"\nReal value of ${nominal} after accounting for {end-start} years of deflation at a rate of {-rate}% per annum is ${real}")

#graphing: x=years, y=value
years = list(range(start, end + 1))
xpoints = np.array(years)
ypoints = np.array(real_values)
plt.xlabel('Value of money ($)', fontsize=12)
plt.ylabel('Year', fontsize=12)
plt.plot(xpoints, ypoints)
plt.show()
