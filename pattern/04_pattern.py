#Given an integer n. You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:

#1
#22
#333
#4444
#55555
# Take input from user and convert it to integer



num = int(input("enter a num: "))

# Outer loop → controls number of rows
# It runs from 1 to num +1
for i in range(1, num + 1):
    
    # Inner loop → prints numbers from 1 to current row number (i)
    for j in range(1,i +1 ):
        
        # Print number without moving to next line
     print(i, end="")
    # After inner loop finishes, move to next line
    print()


#another method "string multiplication"

n = int(input("enter a num: "))

for i in range(1, n + 1):
# converting int to str     
    print(str(i) * i)    