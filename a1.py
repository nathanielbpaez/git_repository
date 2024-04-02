'''
auth @ Nathaniel B. Paez
student_ID: 501228087
date: 2024/03/19

The objective of this program is to be a calculator in preperation for MTH108 Linear algebra

The following program is equipped to swiftly solve both simple and complex concepts.
The program will ask you; what you would like to do. If you choose a vector option,
you will pre required to input 2 3d vectors.

Should you enter a zero vector or the same vector twice, the calculator will return a zero vector
or a variable displaying it's equal to itself.
'''

#imports
import math as m
from datetime import datetime as dt
import numpy as np

# UPON OPEN / MAIN FUNCTIONALITY

def upon_open(): #runs to record dates
    with open('output.txt', 'a') as vector_history:
        vector_history.write('\nDate edited: ' + str(dt.now()) + '\n')

#determine what calculator the user wants to use
def main(): #everything is ran through vector checker to allow for optimal function calling
    #options
    print ("\nWhat vector related question would you like to calculate?\n")
    print (" 0. Write additional notes") 
    print (" 1. Do you want to know the angle between two 3D vectors?")
    print (" 2. Do you want to know the area of the parallelogram from two 3D vectors?")
    print (" 3. Do you want to know the cross product of two 3D vectors?")
    print ("-1. Clear history (NOTE: CANNOT UNDO)\n")

    #for future reference: insert new equations here

    checker = int(input("Please select a number corsponding to the previous list: "))
    with open('output.txt', 'a') as vector_history: #REFER TO LINE 18
        # 0. FREE WRITE
        if checker == 0:
            vector_history.write("\n" + str(input("NOTES: \n")) + "\n")

        # 1. ANGLE
        if checker == 1:
            angle, a, b = vector_angle()
            vector_history.write(f'\nThe angle between vectors {a} and {b} is {angle}\n')
        
        # 2. AREA OF PARALLELOGRAM
        if checker == 2:
            aOfv, a, b = vector_area()
            vector_history.write(f'\nThe area of the parallelogram in vectors {a} and {b} is {aOfv}\n')

        # 3. CROSS PRODUCT
        if checker == 3:
            cross_prod, a, b = cross_prod_calc()
            vector_history.write(f'\nThe cross product of {a} and {b} is {cross_prod}\n')

        # -1. CLEAR
    if checker == -1:
        with open('output.txt', 'w') as vector_history:
            vector_history.write("")
    repeat()
    return

#repeat function (allows for constant edits)
def repeat(): #repeats to allow for more calculations in one run
    switch = False
    x = str(input("\nWould you like to do anything else? (Y/N): "))
    if x == "Y":
        switch = True
        if switch == True: #I needed boolean some how
            main() #recycles
    elif x == "N":
        return #exits program
    else:
        print('Incorrect input please try again.') #to make sure no error.
        return repeat()
    return
    
# this function will be called, and will ask the user for their inputs
def vector_bucket():
    vect = [[],[]]
    for i in range (2):
        vect[i].append(int(input(f"Enter X{i+1}: ")))
        vect[i].append(int(input(f"Enter Y{i+1}: ")))
        vect[i].append(int(input(f"Enter Z{i+1}: ")))

    #Checks for zero vectors since 0/b or a/0 does not work
    if vect[0] == [0, 0, 0] or vect[1] == [0, 0, 0]: 
        print("Error: a zero vectors in regards to a vector equals zero")
        return "Zero Vector"
    elif vect[0] == vect[1]:
        print("Error: there is no value between the same vector.")
        return "Equal Vectors"
    return vect

# EQUATIONS

#The equation for the angle of the vector is ((a*b) / (|a||b|))* cos^-1
def vector_angle():
    vect = vector_bucket()
    a = vect[0]
    b = vect[1]
    if vect == "Zero Vector":
        return [0, 0, 0], "A", "a zero vector" 
    elif vect == "Equal Vectors":
        return a, a, a

    # calculate a*b
    a_b = []
    for i in range (3):
        a_b.append(a[i]*b[i])
    a_b = sum(a_b)
    
    # calculates the magnitude of both vectors
    a_mag = [] #open lists to append the squared values
    b_mag = []
    for i in range (3): #loop to square the values
        a_mag.append(a[i]**2)
        b_mag.append(b[i]**2)
    #calculatoing |a|*|b|
    a_mag = m.sqrt(sum(a_mag))
    b_mag = m.sqrt(sum(b_mag))  
    #calculates the sum
    a_b_diff = a_mag * b_mag #multiplies magnitudes
    arb_k = (a_b/a_b_diff)
    theta = m.acos(arb_k) #automatically casts from degree to rad
    theta = round(measurement_checker(theta), 4) #this rounds the answer to 4 decimal points regadless if rad or deg
    return theta, a, b

#The equation for the area of the parallelogram from two vectors (dot prod of 2 vects)
def vector_area():
    vect = vector_bucket() #call for vector information
    if vect == "Zero Vector":
        return [0, 0, 0], "A", "a zero vector" 
    elif vect == "Equal Vectors":
        return a, a, a
    
    a = vect[0] # is the first set of coords
    b = vect[1] # is the second set of coords

    a_b_cross_prod = cross_product(a, b) #calls cross prod func
    area_of_vector = m.sqrt(sum(x**2 for x in a_b_cross_prod)) #calculates the magnitude of cross prod
    area_of_vector = round(area_of_vector, 4)# rounds the value
    return area_of_vector, a, b

def cross_prod_calc():
    vect = vector_bucket()
    if vect == "Zero Vector":
        return [0, 0, 0], "A", "a zero vector" 
    elif vect == "Equal Vectors":
        return a, a, a
    
    a = vect[0]
    b = vect[1]
    a_b_cross_prod = cross_product(a, b)
    return a_b_cross_prod, a, b
# SUB EQUATIONS

# when called it either returns from prev inputed rad or casts to deg
def measurement_checker(theta):
    checker = (str(input('\nDo you want the answer in degrees or radians?\nPlease type either "deg" or "rad": ')))
    # verify user intent
    if checker == "deg":
        return m.degrees(theta)
    elif checker == "rad":
        return (theta)

# used as a quick function to calculate the cross products and returns as a new list (the dot prod)
def cross_product(a, b):
    x = (a[1]*b[2]) - (a[2]*b[1])
    y = (a[2]*b[0]) - (a[0]*b[2])
    z = (a[0]*b[1]) - (a[1]*b[0])
    return [x, y, z]


if __name__ == "__main__":
    upon_open() #watermarks the date
    main() #main function call
