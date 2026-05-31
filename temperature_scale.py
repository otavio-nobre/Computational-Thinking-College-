#Create a program that reads a temperature value and its scale, converts it, and displays that temperature in all three main scales 
# Celsius, Fahrenheit, and Kelvin).

temperature = float(input("Enter the temperature value:"))
scale = input("What is the current scale?(c, k, f):").upper()

if(scale == "C"):
    print("Temperature in Celsius:", temperature)
    print("Temperature in Fahrenheit:", round((temperature*1.8)+32, 2))
    print("Temperature in Kelvin", round((temperature + 273.15),2))
elif(scale == "K"):
    print("Temperature in Celsius:", round((temperature-273.15),2 ))
    print("Temperature in Fahrenheit:", round((((temperature - 273.15)*1.8)+32),2))
    print("Temperature in Kelvin", temperature)
else:
    print("Temperature in Celsius:", round(((temperature-32)/1.8,2)))
    print("Temperature in Fahrenheit:", temperature)
    print("Temperature in Kelvin", round((((temperature-32)/1.8)+273.15,2)))


