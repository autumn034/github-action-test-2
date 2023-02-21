#factorial.py gets the factorial of given user number
def factorial(number):

    factorial = 1

    # check if the number is negative, positive or zero
    if number < 0:
        return("Please enter a positive number.")
    elif number == 0:
        return(1)
    else:
        for i in range(1,number + 1):
            factorial = factorial*i
        return(factorial)
   

