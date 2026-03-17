# Take input from user
n = int(input("Enter n: "))

# Loop through rows
for i in range(n):

    # Loop through columns
    for j in range(n):

        # Print '*' for borders
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            # Print space inside
            print(" ", end="")

    # Move to next line after each row
    print()