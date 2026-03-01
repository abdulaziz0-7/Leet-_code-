# Given an integer n. You need to recreate the pattern given below for any value of N. 
# Let's say for num = 5, the pattern should look like as below:

# *
# **
# ***
# ****
# *****

# creating a variable num initilizing num as intiger getting input from user
num =int(input("enter a num"))
# creating a for loop i as beginning range and num+1 as end of range
# 0 is beging range and num+1 is ending range
for i in range (num+1):
# printing "*" * i     
    print("*"*i)

