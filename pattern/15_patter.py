n = int(input("Enter n: "))

#creating a for loop star from n , stops at 0 and ad step as -1
for i in range(n, 0 , -1):
    
    for j in range(i):
        print(chr(65 + j), end="")
    print()
