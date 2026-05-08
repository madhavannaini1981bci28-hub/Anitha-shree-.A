n=int(input("enter a No. : "))
if (n%2==1):
    print("Weird")
if(n%2==0):
    if(2<=n and n<=5):
        print("Not Weird")
    elif(6<=n and n<=20):
        print("weird")
    elif(n>20):
        print("Not Weird")
        
