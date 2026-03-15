n = int(input("Enter n: "))

for i in range(0, n+1 ):
    
    for j in range(i):
        print(chr(64 + i), end="")
    print()