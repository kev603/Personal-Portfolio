# assignment 3
# program that will calulate the speeding fine
# fine doubles if in a school/construction zone

def SuarezSpeedLimit():
    input("Welcome to program that calculates the speeding fine")
# speed = speed of vehicule
# speedLimit = speed limit
# spd_diff = speed difference/ how much over/under the speed limit
    speed = eval(input("Please input the speed in mph: "))
    speedLimit = eval(input("Please input the speed limit in mph: "))
    spd_diff = speed - speedLimit
    over_limit = False
    cOrSZone = False
    
    if spd_diff <= 0: # if the difference is negative or == 0, you are at the speed limit
        over_limit = False # means at or under speed limit
    else:
        over_limit = True # means over the speed limit
#   if at the speed llimit
    if over_limit == False:
        print("You are at the speed")
    else: # if the difference is over 0, you are over the speed limit
        over_limit = True 
#   if over the speed limit
    if over_limit == True:
        print("You are over the speed limit")
        sch_cons = input("Please say yes or no if it is a School/Construction Zone: ")
    
    if sch_cons == "no" or sch_cons == "No":
        cOrSZone = False # meaning no construction/school zone
    elif sch_cons == "yes" or sch_cons == "Yes":
        cOrSZone = True # meaning there is a construction/school zone
        zone = input("Please specify which zone: School/Construction Zone: ")
    else:
        print("wrong input")
#   if there is no construction/school zone
    if cOrSZone == False and spd_diff > 0 and spd_diff < 10:
        print("Your fine is $120.00 \t Slow down. !")
    elif cOrSZone == False and spd_diff >= 10 and spd_diff < 15:
        print("Your fine is $199.00 \t Drive with caution. !")
    elif cOrSZone == False and spd_diff >= 15 and spd_diff < 20:
        print("Your fine is $248.00 \t You are over speeding. !")
    elif cOrSZone == False and spd_diff >= 20 and spd_diff < 30:
        print("Your fine is $286.00 \t You are in Danger Zone. !")
    elif cOrSZone == False and spd_diff >= 30:
        print("Court is Mandatory \t See ya in court. !!")
#   if there is a construction/school zone
    if cOrSZone == True and spd_diff > 0 and spd_diff < 10:
        fine1 = 120.00 * 2
        print(zone,"\t Your fine is","$",fine1,"\t Slow down. !")
    elif cOrSZone == True and spd_diff >= 10 and spd_diff < 15:
        fine2 = 199.00 * 2
        print(zone,"\t Your fine is","$",fine2,"\t Drive with caution. !")
    elif cOrSZone == True and spd_diff >= 15 and spd_diff < 20:
        fine3 = 248.00 * 2
        print(zone,"\t Your fine is","$",fine3,"\t You are over speeding. !")
    elif cOrSZone == True and spd_diff >= 20 and spd_diff < 30:
        fine4 = 286.00 * 2
        print(zone,"\t Your fine is","$",fine4,"\t You are in Danger Zone. !")
    elif cOrSZone == True and spd_diff >= 30:
        print(zone,"\t Court is Mandatory \t See ya in court. !!")

SuarezSpeedLimit()
