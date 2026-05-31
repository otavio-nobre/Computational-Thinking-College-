#Make a program that reads the value of a purchase and the payment option (V – for cash payment or P – for installment payment).
#If the customer pays in cash, he will have a 5% discount, if he pays in 3 installments he will have an increase of 8%. 
#The program must show the purchase amount and the cash value or term value (total amount and the value of each installment).

value = int(input("Enter the purchase value: "))
payment_option = input("How will you pay? (p,v) ").upper()

if payment_option == "P":
    total_value = value * 1.08
    installment = total_value / 3
    
    print("You will pay:", total_value)
    print("Installment 1:", installment)
    print("Installment 2:", installment)
    print("Installment 3:", installment)
else:
    total_value = value * 0.95
    print("You will pay:", total_value)