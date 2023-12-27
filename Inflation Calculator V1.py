#calculated assuming there is a static rate of inflation i.e. inflation rate is the same for all years
#no validation/checking methods implemented

nominal = float(input("Enter initial value/amount money in $: "))
start = int(input("Enter start year: "))
end = int(input("Enter end year: "))
rate = float(input("Enter rate of inflation (%): "))

real = round((nominal/(1+(rate/100))**(end-start)), 2)
print(f"\nReal value of money after accounting for {end-start} years of inflation at a rate of {rate}% per annum is ${real}")
