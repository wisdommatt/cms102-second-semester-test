# Project Title: CMS102 Group 2 Test Project.
# ---------------------------------------------------------------------
# Project Description: | Write a program that will ask the user to    |
# .................... | enter an integer less than 50 and then print |
# .................... | whether or not the integer is prime.         |
# ---------------------------------------------------------------------
# Course Lecturer: MR. ORIJI
# ---------------------------------------------------------------------
# Course Code: CMS-102
# ---------------------------------------------------------------------
# Department: Computer Science
# ---------------------------------------------------------------------
# Faculty: Science
# ---------------------------------------------------------------------


# ======================================================================
#                       PSEUDO CODE
# ======================================================================
# 
#   STEP 1: Ask the user to input a number.
#   STEP 2: Assign the user input to a variable 'num'.
#   SETP 3: Check if num is a digit or number because num must be a digit.
#   STEP 4: Check if num is less than 50.
#   STEP 5: Print error to the user if num is greater than or equal to 50 because 
#           the project description specified less than 50.
#   STEP 6: Interate from the integer 2 to num - 1.
#   STEP 7: Check if num modulus the current iteration value is equal to 0.
#   STEP 8: If num modulus the current iteration value is equal to 0 break out of 
#           the loop and print that the number is a prime number.
#   STEP 9: If the loop ends and num modulus any iteration value is not equal to zero (0)
#           print that the number is not a prime number.

def prime_calculator():
    number = 50
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            print (i)
            is_prime = False

    print(is_prime)

prime_calculator()