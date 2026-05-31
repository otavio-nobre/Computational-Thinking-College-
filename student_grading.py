#Calculate a student's weighted final grade based on three units (N1​, N2​, N3​) and determine their academic status (Passed, Failed, or Final Exam).

grade1 = float(input("Enter your grade 1:"))
grade2 = float(input("Enter your grade 2:"))
grade3 = float(input("Enter your grade 3:"))
median = ((grade1*2)+(grade2*3)+(grade3*4))/9

if(median >= 7):
    print("Aproved")
elif(median < 7 and median >= 3):
    print("Final test")
else:
    print("Reproved")

