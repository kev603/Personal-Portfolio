#program that prints the song of Old MacDonald
#it will print the song 3 times 
#each time with a different animal and sound


def main():
    print("Welcome to program that prints out Old Macdonald lyrics") #this is the welcome string
    
    animal1 = "dog" # this is animal 1
    sound1 = "woof" # this is the sound that animal 1 makes

    animal2 = "chicken"
    sound2 = "cuack"

    animal3 = "frog"
    sound3 = "croak"


    nurseryRhymeMacDonald(animal1, sound1) # this is verse 1 with animal 1 and sound 1
    nurseryRhymeMacDonald(animal2, sound2) # in each of these, the verse repeacts but switching the animals 
    nurseryRhymeMacDonald(animal3, sound3) # and the sound they make in response to the variables in them 

#   this is what is inside the function
def nurseryRhymeMacDonald(animal1, sound1):
    print("\n\t Old Macdonald had a farm, E-I-E-I-O")
    print("\t And on his farm he had a",animal1+", E-I-E-I-O")
    print("""\t With a "{0}-{1}" here and a "{2}-{3}" there """.format(sound1,sound1,sound1,sound1)) # i used the .format in order for it to print it as in ""and with a "-"
    print("""\t Here a "{0}" there a "{1}" """.format(sound1, sound1))
    print("""\t Everywhere a "{0}-{1}" """.format(sound1, sound1))
    print("\t Old Macdonald had a farm, E-I-E-I-O")

main()
