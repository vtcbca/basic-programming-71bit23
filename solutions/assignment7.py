n=int(input("Enter an Number"))
num = 1
for i in range(1, n + 1):
    print('  ' * (n - i), end=' ')  
    for j in range(1, 2 * i):  
        print(j, end="  ")
    print() 