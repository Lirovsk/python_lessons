# this file is aimed to work with input and output in python
actual_year = 2024
name = input("Enter your namer: ")
age = input("Hi, "+ name +"! Please enter your age: ")
year_of_birth = actual_year - int(age)

print(f"Hi, {name}! You were born in {year_of_birth}")

print("If we were goint to make a form to save your informations, we could use this format to save your data:")
print(name, age, year_of_birth, sep = "-", end = " \n")