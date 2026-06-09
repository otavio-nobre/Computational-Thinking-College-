#This is a program that must calculate the factorial of a number greater than 0

number = int(input("Enter the number:"))
fatorial = 1

if(number == 0):
    print("The number must be greater than 0.")
else:
 while number > 1:
   fatorial = fatorial*number
   number = number - 1

 print(f"The factorial is: {fatorial}")