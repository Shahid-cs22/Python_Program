a=[]
print("Enter 10 Number:")
for i in range(5):
    num=int(input("Enter the Number "+str(i+1)))
    a.append(num)
print(a)
 
sum=0
for i in a:
    sum=sum+i
print("Sum of the given number is:",sum)
