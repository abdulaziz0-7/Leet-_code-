# Given an integer n. You need to recreate the pattern given below for any value of N.
#  Let's say for N = 5, the pattern should look like as below:

# *****
# ****
# ***
# **
# *



# creating a variable num initilizing num as intiger getting input from user
num =int(input("enter a num"))
# creating a for loop 
# 0 is beging range and num+1 is ending range
# inside the range()
# range(start, stop, step)
# 5 is start, 0 is stop , and -1 is step 
# it first minus 5-1 to 4 and 4-1 to 3 and 3-1 to 2  and 2-1 to 1 and ends at 0 as o is referd as stop
for i in range (5,0,-1):
# printing "*" * i     
    print("*"*i)
