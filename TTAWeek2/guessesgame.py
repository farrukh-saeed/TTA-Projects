#FS week2 TTA

guesses = 0
# program is limited to 6 guesses

while guesses < 6:
    guesses = guesses + 1
    print("Take a guess . ")
    guess = int(input())
    if guess < guesses:
        print('Your guess is too low .')
    if guess > guesses:
        print('Your guess is too high ')
    if guess == guesses:
        break
