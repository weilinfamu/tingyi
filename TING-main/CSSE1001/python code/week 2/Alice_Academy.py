import random
  num_answer = 0
while num_answer < 10:
    x = random.randint(10,99)
    y = random.randint(10,99)
    answer = x + y
    
    question = (str(x) + '+' +str(y) + '=')
    guess = int(input(question)
   
        if guess == answer:
            print('Correct')
        else:
            print('No, the correct answer is', answer)
            num_answer += 1
