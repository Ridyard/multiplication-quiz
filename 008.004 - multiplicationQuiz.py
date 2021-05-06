# atbs - timed multiplication quiz

import random, time, pyinputplus as ip

noQs = 10
correctAnswers = 0

difficulty = ip.inputMenu(['easy','medium','hard']) # provide options to user
if difficulty == 'easy':
    t = 10  # t will represent the time allocated for each guess
elif difficulty == 'medium':
    t = 5
else:
    t = 3
    

for i in range(noQs):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)

    q = ('\n#%s: what is %s x %s?\n' % (i+1, num1, num2))
    try:
        guess = ip.inputInt(prompt=q, timeout=t, limit=2)
        result = num1*num2
        if guess == result:
            print('correct!')
            correctAnswers += 1
        else:
            print('nope, the correct answer is ' + str(result))
    except ip.TimeoutException:  # exceptions are in the pyinputplus module
        print('too slow... the answer is ' + str(num1*num2))
    except ip.TimeoutException:
        print('out of tries...')
    time.sleep(2) # allow a brief pause between questions

    
print('\nyou scored %s/%s' % (correctAnswers, noQs))
if correctAnswers > 8:
    print('well done!')
elif correctAnswers < 4:
    print('try harder...')



