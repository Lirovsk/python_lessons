#Working and learning how to manipulate strings in Python
name = "João"
age = 20
language = "Python"

# using different ways to interpolate variables in strings

#old style
print("My name is %s, I'm %i years old and I'm learning %s" % (name, age, language))
print()
print()

#format
print("My name is {}, I'm {} years old and I'm learning {}".format(name, age , language))
print()
print("My name is {2}, I'm {0} years old and I'm learning {1}".format(age, language, name))
print()
print()
#f-string
print(f"My name is {name}, I'm {age} and I'm learning {language}")