# Take input
n = int(input("Enter n: "))

# Loop through rows
for i in range(n):
    
    # Starting character for each row
    # Example: i=0 → E, i=1 → D, ..., i=4 → A
    start = 65 + (n - i - 1)
    
    # Loop to print characters from start to E
    for j in range(start, 65 + n):
        print(chr(j), end=" ")
    
    # Move to next line
    print()