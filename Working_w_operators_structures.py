#in this file I'm amimng to work with operators in python, so, in somtimes, I won't use the sortest way to solve a problem.
import time as t
import sys
#Variable Declaration
my_name = "Joao"
my_weight = 80
output_user = [[False] *5, [False] *5, [False] *5]
outout_user2 = 0
#This varible contain the nutricional value of some food and what time of the day it is suposed to be eaten
inside_fridge = [["orange", "rice and beans", "corn flakes", "coffe", "banana" ]
                 ,[62, 220, 170, 10, 89]
                 ,["afternoon break", "lunch and dinner", "breakfast", "breakfast", "afternoon and morning break"]]

#Input of some user data

im_hungry = input("Hi "+ my_name + ", Are you hungry?\n")

if (im_hungry == "yes") or (im_hungry == "Yes") or (im_hungry == "y") or (im_hungry == "Y") or (im_hungry == "yep") or (im_hungry == "Yep"):
    im_hungry = True
else:
    im_hungry = False

if im_hungry:
    time_now = int(input("What time is it now? "))
    if time_now >6 and time_now <9:
        time_eat = "breakfast"
        print("It is breakfast time!")
        t.sleep(0.7)
        for i in range(0,4): 
            if inside_fridge[2][i] == time_eat:
                output_user[2][i] = True
        print("In the frezer we have ")
        for i in range (0,4):
            if output_user[2][i] == True:
                print( inside_fridge[0][i])
                sys.stdout.flush()
        t.sleep(0.4)
        print(" Thanks for using this program ".center(70, "#"))
        print("Exiting", end = "")
        sys.stdout.flush()
        for i in range(0,3):
            print(".", end= "")
            sys.stdout.flush()
            t.sleep(0.5)              

    elif time_now >= 9 and time_now < 11:
        print("It is morning break time!")
        t.sleep(0.7)
        for i in range(0,4): 
            if "morning break" in inside_fridge[2][i]:
                output_user[2][i] = True
        print("In the frezer, for morning break, we have: ", end= "")
        for i in range (0,4):
            if output_user[2][i] == True:
                    print( inside_fridge[0][i])
                    sys.stdout.flush()
        t.sleep(0.5)
        print ("but you can also eat ")
        for i in range (0,4):
            if (output_user[2][i] == False) and ("break" in inside_fridge[2][i]):
                print( inside_fridge[0][i])
                sys.stdout.flush()
        t.sleep(0.4)
        print(" Thanks for using this program ".center(70, "#"))
        print("Exiting", end = "")
        sys.stdout.flush()
        for i in range(0,3):
            print(".", end= "")
            sys.stdout.flush()
            t.sleep(0.5)

    elif time_now >= 12 and time_now < 14:
        print("It is lunch time!")
        t.sleep(0.7)
        for i in range (0,4):
            if "lunch" in inside_fridge[2][i]:
                output_user[2][i] = True
        print("In the frezer, for lunch, we have: ", end = "")
        for i in range (0,4):
            if output_user[2][i] == True:
                print( inside_fridge[0][i])
                sys.stdout.flush() 
        t.sleep(0.4)
        print(" Thanks for using this program ".center(70, "#"))
        print("Exiting", end = "")
        sys.stdout.flush()
        for i in range(0,3):
            print(".", end= "")
            sys.stdout.flush()
            t.sleep(0.5)

    elif time_now >= 14 and time_now < 18:
        print("It is fternoon break time!")
        t.sleep(0.7)
        for i in range(0,4): 
            if "fternoon break" in inside_fridge[2][i]:
                output_user[2][i] = True
        print("In the frezer, for fternoon break, we have: ", end = "")
        for i in range (0,4):
            if output_user[2][i] == True:
                print( inside_fridge[0][i])
                sys.stdout.flush()
        t.sleep(0.5)
        print ("but you can also eat ")
        for i in range (0,4):
                if (output_user[2][i] == False) and ("break" in inside_fridge[2][i]):
                    print( inside_fridge[0][i])
                    sys.stdout.flush()
        t.sleep(0.4)
        print(" Thanks for using this program ".center(70, "#"))
        print("Exiting", end = "")
        sys.stdout.flush()
        for i in range(0,3):
            print(".", end= "")
            sys.stdout.flush()
            t.sleep(0.5)

    elif time_now >= 19 and time_now < 22:
        time_eat = "dinner"
        print("It is dinner time!")
        t.sleep(1)
        for i in range (0,4):
            if "dinner" in inside_fridge[2][i]:
                output_user[2][i] = True
        print("In the frezer, for dinner, we have: ", end = "")
        for i in range (0,4):
            if output_user[2][i] == True:
                print( inside_fridge[0][i])
                sys.stdout.flush()
        t.sleep(0.4)
        print(" Thanks for using this program ".center(70, "#"))
        print("Exiting", end = "")
        sys.stdout.flush()
        for i in range(0,3):
            print(".", end= "")
            sys.stdout.flush()
            t.sleep(0.5)

    elif time_now==11 or time_now==18:
        t.sleep(0.4)
        print("It is too close to the next meal, you should wait a little bit more")
        t.sleep(0.4)
        print(" Thanks for using this program ".center(70, "#"))
        print("Exiting", end = "")
        sys.stdout.flush()
        for i in range(0,3):
            print(".", end= "")
            sys.stdout.flush()
            t.sleep(0.5)

    else:
        t.sleep(0.4)
        print("You should not eat now, go to sleep")
        t.sleep(0.4)
        print(" Thanks for using this program ".center(70, "#"))
        print("Exiting", end = "")
        sys.stdout.flush()
        for i in range(0,3):
            print(".", end= "")
            sys.stdout.flush()
            t.sleep(0.5)
else: 
    t.sleep(0.4)
    print("It is okay then")
    t.sleep(0.4)
    print(" Thanks for using this program ".center(70, "#"))
    print("Exiting", end = "")
    sys.stdout.flush()
    for i in range(0,3):
        print(".", end= "")
        sys.stdout.flush()
        t.sleep(0.5)