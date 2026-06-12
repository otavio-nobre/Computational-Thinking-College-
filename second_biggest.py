numbers_list = []

print("Send 'exit' to end your program!")

while True:
    user_input = input("Enter the numbers: ")
    
    if user_input.lower() == "exit":
        break
    
    number = float(user_input)
    numbers_list.append(number)

numbers_list.sort()

second_biggest = numbers_list[-2]

print(f"The second biggest value is: {second_biggest}")