# Take input from the user and convert it into an integer
n = int(input("Enter n: "))

# Outer loop: controls the number of rows
# range(0, n+1) means the loop runs from 0 to n
for i in range(0, n+1):

    # Inner loop: controls how many times the letter prints in each row
    # range(i) means it runs i times
    for j in range(i):

        # chr(64 + i) converts a number to a letter using ASCII
        # Example:
        # i = 1 → chr(65) → A
        # i = 2 → chr(66) → B
        # i = 3 → chr(67) → C
        # end="" keeps printing on the same line
        print(chr(64 + i), end="")

    # After finishing printing letters in a row,
    # print() moves the cursor to the next line
    print()