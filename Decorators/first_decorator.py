# In the first example, I'm goint to use a subtraction function to be used with the decorator, the decorator will be used to ensure the B value is never greater than the A value
def dacorator(func):
    def wrapper(a, b):
        if b > a:
            raise ValueError("B cannot be greater than A")
        return func(a, b)
    return wrapper

@dacorator
def sub(a, b):
    return a - b

print(sub(10, 5))  # This will work fine
print(sub(5, 10))  # This will raise a ValueError
print(sub(10, 10))  # This will work fine too