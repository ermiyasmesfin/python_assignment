def evaluator():
    positive = []
    negative = []
    while(True):
        
        input_num = int(input('Enter any number, the program exits if input is 0: '))
        if input_num > 0:
            positive.append(input_num)
        else:
            negative.append(input_num)
        if input_num == 0:
            print('The number of positives is {}\nThe Numbers are: {}'.format(len(positive), positive))
            print('The number of negatives is {}\nThe Numbers are: {}'. format(len(negative), negative))
            
            print('The total is {}'.format(sum(positive)+sum(negative)))
            print('The average is {} '.format((sum(positive)+sum(negative))/(len(positive)+len(negative))))
            break
            
evaluator()