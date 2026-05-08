for row in range(0,5):
    for col in range(0,5):
        if(row==0 and col in {0,3}):
            print('$',end=' ')
        elif(row==1 and col in {0,2}):
            print('$',end=' ')
        elif(row==2 and col in {0,1}):
            print('$',end=' ')
        elif(row==3 and col in {0,2}):
            print('$',end=' ')
        elif(row==4 and col in {0,3}):
            print('$',end=' ')
        else:
            print(' ',end=' ')
    print()
