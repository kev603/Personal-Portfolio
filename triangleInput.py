#this program will calculate the area of a triangle
#by asking the user to input the values of the sides of the triangle
#the program will also check if the inputs are valid
#if the inputs are not valid, then the pogram will ask the user to input the
#values again until it sees that they are valid
#then once the inputs are valid, it will take the inputs to calculate the
#area of the triangle


print("""\t"Welcome to program that calculates the Area of a Triangle" """)#welcome string
def triangleInput():    #main function call
#prompt for the user to enter the input values
    a,b,c = eval(input("Please enter the sides of the triangle as a,b,c: "))

    isValid(a,b,c)#function call that checks for the values to be valid
    calcArea(a,b,c)#function call that makes the calculations to find the area

#here the program checks if the inputs are valid
def isValid(x,y,z):
    sum = x + y #if the sum of the first two inputs is greater than or equal to
                #the last inout, then the inputs are invalid and useer must enter inputs again
    while sum <= z:
        print("Invalid Input. Try Again")
        triangleInput()
        return
#if the sum is less than the last input number, then the inputs are valid
#and the program will print "valid" as a way to let the user know
    if sum > z:
        print("Valid Input")

#here the program calculates the are using the input values after being checked
def calcArea(x,y,z):
    import math  #use this method to calculate the square root
    s = ((x + y + z)/2) # formula to find the value of "s", which is needed for the next step
    a1 = s*(s - x)*(s - y)*(s - z)
    if a1 > 0:
        area = math.sqrt(a1)#this is the next step, or formula in which the "s" was needed
        print("The area of the triangle is {0:0.3f}".format(area)) #prints out the final result
                                                       #which is the area of the triangle


triangleInput()

print("Byee!!")#final greeting. shows the user that the calculations have
               #been complete
