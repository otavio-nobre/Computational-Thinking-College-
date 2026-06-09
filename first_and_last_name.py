outputs = []

for _ in range(4):
    name_complete = input("Enter the names:")
    names = name_complete.split()
    
    first_name = names[0]
    last_name = names[-1]
    
    outputs.append(f"First name: {first_name} | Last name: {last_name}")

for result in outputs:
    print(result)