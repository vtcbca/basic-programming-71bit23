num=int(input("Enter an Number to check number is prime or not  ="))
number=0
if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
             number= 1
             break
if number== 1:
  print(num,' is Not Prime')
else:
  print(num,"is Prime")

                 
     
 