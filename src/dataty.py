# DH = 734_529.678

# print(type(DH))

#Calculate the BMI of a person

Weight = input("Enter your weight in kg: ")

Height = input("Enter your height in meters: ")


BMI = float(Weight) / (float(Height) ** 2)

print("Your BMI is: ", round(BMI, 2))