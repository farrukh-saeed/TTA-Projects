import random
while True : # program will continue running unless press enter or enter empty
    print()

    usersQuestion = input('Please think of a number between 1 to 10 or Enter to quit the program : ')
    if usersQuestion == '' :
        break

    randomNumber = random.randrange(10)

    if randomNumber == 1 :
        print ('Congratulations ! You are on the first place')
    elif randomNumber == 2 :
        print ('Excellent ! you are on the second place')
    elif randomNumber == 3 :
        print (' Weldone You are on the 3rd place')
    elif randomNumber == 4 :
        print ('Good you are on 4th place')
    elif randomNumber == 5 :
        print ('Nice you are on 5th place')
    elif randomNumber == 6 :
        print ('Better you are on 6th place')
    elif randomNumber == 7 :
        print (' Try again you are on 7th place')
    elif randomNumber == 8 :
        print ('Work hard you are on 8th place')
    elif randomNumber == 9 :
        print ('You hardly tried, you are on 9th place')
    elif randomNumber == 10 :
        print (' Fail')