# Given an integer n. You need to recreate the pattern given below for any value of N. 
#  Let's say for N = 5, the pattern should look like as below:

# A
# AB
# ABC
# ABCD
# ABCDE

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
