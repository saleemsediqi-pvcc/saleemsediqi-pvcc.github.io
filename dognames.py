# Name: Jazil Choudhry
# Prog Purpose: This program demonstrates how to manipulate a list, including:
# finding number of items in the list, sorting the list, adding/removing items,
# copying a list of items into another list, and changing the data in the list.

dogs = ["Sadie", "Molly", "Ella", "Milo",
        "Gonzo", "Sweetie-Pie","Buddy", "Rocky", "AnnaBelle", "Diego"]
dogs2 = []

def main () :
    how_many = len (dogs)
    print ("\nNumber of dogs in the list: " + str (how_many))
    print ("\nOriginal list of dog names:")
    print (dogs)

    dogs.reverse ()
    print ("\list from last to first:")
    print (dogs)
    
    dogs.sort ()
    print ("\Alphabetized list:")
    print (dogs)
    
    dogs.sort (reverse = True)
    print ("\List in reverse alphabetized order:")
    print (dogs)
    
    dogs.append ("Ranger")
    print ("\nAdd a dog to the end of a list:")
    print (dogs)
    
    doggy = dogs.pop (0)
    print ("\nPop a dog off (remove) from the front of the list:")
    print (dogs)
    print (doggy + " was removed from the front of the list.")
    
    another_dog = dogs.pop (3)
    print ("\nNote: Position numbers in a list begin with 0, not with 1")
    print ("Pop a dog off from position 3 (which is the 4th dog) in the list:")
    print(dogs)
    print(another_dog+ " was removed from position 3 of the list.")

    dogs.remove('AnnaBelle')
    print("\nRemove a dog by name rather than position in the list:")
    print(dogs)

    dogs2= dogs
    print("\nA list can be copied into another list by setting one equal to the other:")
    print(dogs)
    print(dogs2)

    print("\nUse a FOR loop to give each dog in the same last name:")
    for i in range(len(dogs)):
          dogs[i]=dogs[i] + "Choudhry"
    print(dogs)

main()
