# SuarezLoop.py
# this program shows the different ways it counts
# either in ascending or descending order
# it will also ask for an input number and either count from that number up or down 
# or it will count untill the input number

def SuarezLoop():

    print("Welcome to program that counts numbers in ascending and descending order.")

#   this loop counts strating from 10 down to 0
    for n in range(10,0,-1):
        print(n, end=" ")
    print("\nThis loop counts from 10 down to 1")
    

    fun2()
    print("This loop counts from 5 up to 100")
    
    fun3()
    print("\nThis loop counts from input number down to 0")
    
    fun4()
    print("\nThis loop counts from 1 up to the input number")
    

# this loop counts from 5-100 and has commas in between each number
def fun2():
    for n2 in range(5,100,5):
        print(n2, end=",")
    print("100")

# this loop counts down from the input number all the way to 0 using a while loop
def fun3():
# count is the input integer parameter
    count = int(input("Please enter an integer: "))
    while count >= 0:
        print(count, end= " ")
        count -= 1

# this loop counts up from 1 all the way to input number using a for loop
def fun4():
    num = int(input("Please enter an integer: "))
    limit = num + 1
    for i in range(1,limit,1):
        print(i, end=" ")
    
SuarezLoop()

