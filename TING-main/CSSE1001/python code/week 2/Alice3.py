import random
num_questions = 0
while num_questions < 10:
    x = random.randint(0,99)
    y = random.randint(0,99)
    
    operation = random.randint(1,6)

    if operation == 1:
        operation = '+'
        answer = x + y
    elif operation == 2:
        operation = '-'
        answer = x - y
    elif operation == 3:
        operation =' * '
        answer = x * y
    elif operation == 4:
        operation = '//'
        answer = x // y
    elif operation == 5:
        operation = ' ** '
        y = random.randint(0,3)
        answer = x ** y
    else:
        operation = ' % '
        answer = x % y
        
        

    question =(str(x) + operation + str(y) + '=')
    guess = int(input(question))

    if guess == answer:
        print('Correct')
    else:
        print('No, the correct answer is', answer)
    num_questions += 1
