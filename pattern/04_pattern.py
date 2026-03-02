# Take input from user and convert it to integer
num = int(input("enter a num: "))

# Outer loop → controls number of rows
# It runs from 1 to num +1
for i in range(1, num + 1):
    
    # Inner loop → prints numbers from 1 to current row number (i)
    for j in range(1,i +1 ):
        
        # Print number without moving to next line
     print(j, end="")
    # After inner loop finishes, move to next line
    print()