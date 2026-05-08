for row in range(0,5):
    for col in range(0,5):
        if(row==0 and col in {0,1,2,3,4}):
            print('$',end=' ')
        elif(row in {1,2,3,4} and col in {0,4}):
            print('$',end=' ')
        elif(row==4 and col in {0,1,2,3,4}):
            print('$',end=' ')
        else:
            print(' ',end=' ')
    print()
