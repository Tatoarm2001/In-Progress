import random
while True:
    num=random.randint(1,10)
    guess=input('Elige un numero del 1 al 10:')

    

    if int(guess) < 1 :
        print('Pick a number between 1 and 10')
    if int(guess) > 10 :
        print('Pick a number between 1 and 10')

    else:
        if guess==num:
            print('Well done')
            break
        else:
            print('Try again')
           

print('The end')
    
    
    
    
    
    
    #print(num)
    #print(guess)