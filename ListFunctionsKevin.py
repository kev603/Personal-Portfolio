#this program asks the user to input a list
#then the list goes through a series of functions as the input parameter

#welcome string
print("""\t"Welcome to program that takes a list as an input parameter!!" """)

#main function
def listFunctionsKevin():#this is the main function
    number_list = listNum() #this is the list that the user inputs
    rangeList(number_list)#outputs the calculated range of the list
    listSum = sumList(number_list)#shows the returned value as the sum of the list
    average(number_list, listSum)#outputs the average value in the list
    median(number_list)#outputs the median value
    clipNum = eval(input("\nEnter a number to Clip the list: "))#asks the user to enter a clip number
    clip(number_list, clipNum)#outputs the clipped list regarding to the clip number


def listNum():  #in this function the user inputs a list of numbers
    number_list = []#here the list is still empty untill the user inputs some values
#here the lim is the lenth of the list, which is the amount of values the user
#wants to put on his/her list
    lim = int(input("\nEnter the number of values in your list: "))
#the count is equivalent to the length, so it must first be set to 0 so that then
#the user can set it to what ever they want it to
    count = 0
#in this while, the user will then be asked to enter numbers until the counter
#is equal to the lim (or lenth)
    while count < lim:
        listValues = eval(input("Enter a number: "))
        number_list.append(listValues)#every number entered by the user gets appended to the list
        count += 1
    print("\nThis is your list:",number_list)
    return number_list #the list values are then returned so that the pc knows that
    #those are the values inside the list

#this function calculates the range of the list
#the range is the giggest value - the smallest value
def rangeList(x):
    maxNum = max(x)
    minNum = min(x)
    range = maxNum - minNum
    print("\nThe Range of the list is: {0}".format(range))

#this function calculates the sum of all the values inside the list
#it takes the list as a parameter
def sumList(n):
    listSum = sum(n)#calculates the sum of the values in the list
    print("\nThe Sum of all the values is: {0:0.2f}".format(listSum))
    return listSum #then it returns the listSum which is the sum of the values

#this function calculates the average value of the list by adding all the values
#together and then deviding the sum by the length of the list
def average(x,y):
    listAve = y / (len(x))#formula for calculating the average
    print("\nThe Average is: {0:0.2f}".format(listAve))

#This function calculates the median of the list and also prints the user's list sorted
def median(m):
    m.sort()
    print("\nThis is your Sorted list:", m)#the user's sorted list
    if len(m) % 2 == 0:#this determines if the length of the list is even or odd
#if the function is even, it needs to find the 2 middle index
        med1 = m[int(len(m)/2)]#this is to find the first middle index
        med2 = m[int(len(m)/2)-1]#this finds the second middle index
        median = (med1 + med2)/2#then it finally calculates the median by adding
#the 2 middle index values and then deviding the sum by 2
    else:#if the length is odd then it just needs to find the middle index
        median = m[int(len(m)/2)]#formula to find the middle index
    print("The Median is: {0:0.2f}".format(median))

#this function gets a number entered by the user as the clip number
#that number will then be substituted with any value in the list that is greater than it
#then it will print a message to the user saying what the clip number is and the clipped list
def clip(a,b):#it takes the list and the clip number
    for i in range(len(a)):#here the variable i will loop throught the values in the list
        if a[i] > b:#if the a certain value in the list is greater than the entered clip number,
            a[i] = b#it will be substituted with the clip number
    print("\nThe Clipped List clipped on number {0} is: {1}". format(b, a))


listFunctionsKevin()

print("\n\t\tGoodByee!")
