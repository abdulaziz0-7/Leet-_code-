# Given an integer n. You need to recreate the pattern given below for any value of N. 
#  Let's say for N = 5, the pattern should look like as below:

# A
# AB
# ABC
# ABCD
# ABCDE

#gettimg input from user
n = int(input("Enter n: "))

#creating a for loop star from 1 , stops n+1
for i in range(1, n + 1):
    
    for j in range(i):
        print(chr(65 + j), end="")
    print()
