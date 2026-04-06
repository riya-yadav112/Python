
# important:

# range(start, stop, step):



""" 
<< Typs of loop - 
 1. For Loop
 2. While Loop

 << Keywords - 
 1. Continue
 2. Break 
 3. How to use conditional statement in loops 


"""


# <<<<<<<<<<<<<<<< FOR LOOP >>>>>>>>>>>>>>>>>>>>>>
# EXAMPLE :1

# for i in range(3,8):
#     if i == 4:
#         break 
#     print(f"Iteration number: {i}")

#EXAMPLE 2:

# name = "Jabalpur"

# for letter in name:
#     print(letter)



# <<<<<<<<<<<<<<< WHILE LOOP >>>>>>>>>>>>>>>>>>> 

# count = 1
# while count < 3:
#     print(f"Counting: {count}")
#     count +=1


#<<<<<<<<<<<< switch/ match cases >>>>>>>>>>>>>>>>>>>>>

# day = int(input("Enter your day number: "))
# match day:

#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case 4:
#         print('Thursday')
#     case 5: 
#         print('Friday')
#     case 6:
#         print('Satday')
#     case 7:
#         print('Sunday')
#     case _: #Default case
#         print("It's also a holiday ")




# EXAMPLE 1:

Name = str(input("Enter your name\n"))

match Name: 
    case "sumit":
        print("You can start your work")

    case 'Raghav':
        print("Wait now till 9 o clock")

    case 'Rajni':
        print('Now go for new department')
    case _: #default case
        print("Today is holiday")
