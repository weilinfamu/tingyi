impart random
num = random. randint(0,100)
print Try to guess the number I am thinking of between 1 and 100.
while true:
    guess = int(input('please enter your guess'))
    #if they are right,we end
    if guess == num:
    print('congr....')

    #if they give up, we end
    elif guess == -1:
        print('the number you were trying'
              'to guess was', num)
        #if they're wrong, say sorry, ask again
        else:
            print('sorry that is not correct')
