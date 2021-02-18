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

def prime_calculator():
    number = 50
    is_prime = True
    for i in range(2, number):
        # print(i)
        if number % i == 0:
            print (i)
            is_prime = False

    print(is_prime)

prime_calculator()