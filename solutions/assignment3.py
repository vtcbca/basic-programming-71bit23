terms=int(input("Enter an Number for number of terms  ="))
N_1 = 0  
N_2 = 1  
count = 0  
if terms <= 0:  
    print ("Please enter a valid number(positive integer) ")  
elif terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", terms, ": ")  
    print(N_1)  
else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < terms:  
        print(N_1)  
        Nth = N_1 + N_2  
        N_1 = N_2  
        N_2 = Nth  
        count += 1  