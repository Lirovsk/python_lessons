# Here I'm defining a function that takes a str as an argument
# In this particular case, the function is set up to print a message to the user
def say_hello (name):
    print(f"Hello {name}")

def say_lets_learn (name):
    print(f"Let's learn {name}")

# here I'm defining a function that takes another function as an argument
# In this particular case the function is set up to call the function passed as an argument
# and pass the string "João" as an argument to that function
def msg_to_joao (funcao):
    return funcao("João")


msg_to_joao(say_hello)
msg_to_joao(say_lets_learn)