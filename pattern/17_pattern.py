# Take input from the user
n = int(input("Enter n: "))

# Loop for each row
for i in range(1, n + 1):

    # Print spaces to center the pyramid
    for j in range(n - i):
        print(" ", end="")

    # Print increasing letters (A, AB, ABC...)
    for j in range(i):
        print(chr(65 + j), end="")

    # Print decreasing letters (BA, CBA...)
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")

    # Move to the next line
    print()