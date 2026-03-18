# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# 5 5 5 5 5 5 5 5 5 
# 5 4 4 4 4 4 4 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 2 1 2 3 4 5 
# 5 4 3 2 2 2 3 4 5 
# 5 4 3 3 3 3 3 4 5 
# 5 4 4 4 4 4 4 4 5 
# 5 5 5 5 5 5 5 5 5

# Take input
n = int(input("Enter n: "))

# Size of the pattern
size = 2 * n - 1

# Loop through rows
for i in range(size):
    
    # Loop through columns
    for j in range(size):
        
        # Find minimum distance from all 4 sides
        top = i
        left = j
        bottom = size - 1 - i
        right = size - 1 - j
        
        # Find the minimum distance
        min_dist = min(top, left, bottom, right)
        
        # Print the value
        print(n - min_dist, end=" ")
    
    # Move to next line
    print()