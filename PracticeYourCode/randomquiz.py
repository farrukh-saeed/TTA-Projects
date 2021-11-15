import random

while True:
    print

    usersQuestion = input('Ask the Magic 8 Ball a question (Enter a number or return to quit : ')
    if usersQuestion == '':
        break  # we're done

    randomAnswer = random.randrange(8)
    if randomAnswer == 0:
        print('You have entered 0 so go to car park')
    elif randomAnswer == 1:
        print('You entered 1 so go to first floor')
    elif randomAnswer == 2:
        print('You have entered 2 so go to second floor')
    elif randomAnswer == 3:
        print(' You have entered 3 so go to dinning floor')
    elif randomAnswer == 4:
        print(' You have entered 4 so go to music room floor')
    elif randomAnswer == 5:
        print(' You have entered 5 so go to Art room')
    elif randomAnswer == 6:
        print(' You have entered 6 so go to sixth floor')
    elif randomAnswer == 7:
        print(' You have entered 7 so go to gym and swim floor')
    elif randomAnswer == 8:
        print(' You are on the roof, please go back to other floors')


