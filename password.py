# Password checker
# By: Fanny Lucas 

# STEP 1:
# Prompt thee user to enter their password
#Check the following:
#  -If the password contains  the letter z
#  -If the  password ends with an !
#  -If the password begins with any uppercase letter
# If yes to all three, print "Accept!"
# If any of these are not true, print "Reject!"

enter_pass = input("Create password:  ")

find_z = "z" in enter_pass 
find_Z = "Z" in enter_pass
exclamation = enter_pass[-1]
find_exclamation = "!" in exclamation
first_char = enter_pass[0]
find_upper = first_char.isupper()


if find_z or find_Z:
    if find_exclamation:
        if find_upper:
            print("Accept!")
        else:
            print("Reject") 
    else:
        print("Reject!")
else:
    print("Reject")




  



