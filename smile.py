for row in range(1,6):
    for col in range(1,6):
        if(row==1 and col in {2,3,4}):
            print('*',end=" ")
        elif(row in{2,3,4} and col in{1,5}):
            print('*',end=" ")
        elif(row==5 and col in {2,3,4}):
            print('*',end=" ")
        elif(row==2 and col in{2,4}):
            print('-',end=' ')
        elif(row==3 and col in {3}):
            print('|',end=" ")
        elif(row==4 and col in{2,3,4}):
            print('-',end=" ")
        else:
            print(' ',end=" ")
    print()
