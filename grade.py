s1=int(input("enter a mark:"))
s2=int(input("enter a mark:"))
s3=int(input("enter a mark:"))
s4=int(input("enter a mark:"))
total=s1+s2+s3+s4
print(total)
avg=total/4
print(avg)
if (avg>75):
    print("grade:distinct")
elif (avg>=60 and avg<75):
    print("grade:first division")
elif (avg>=50 and avg<60):
    print("grade:second division")
elif (avg>=40 and avg<50):
    print("grade:third division")
else:
    print("fail")
