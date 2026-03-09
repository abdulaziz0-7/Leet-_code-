# Given an integer n. You need to recreate the pattern given below for any value of N.
#  Let's say for N = 5, the pattern should look like as below:

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

# we get the value of n from the user and store it in a variable n    
n= int(input("enter a number:"))

# creating a for loop to print first half of the pattern by  setting the range from 1 to n+1 and incrementing by 1
for i in range(1,n+1,1):
# first we print "*" multiplying it with i then adding space by multiplying " " with n-1 thena again multiplying " " with n-1 and adding "*" multiplyed wit i   
    print("*"*i +" "*(n-i)+" "*(n-i)+"*"*i) 
# creating a for loop to print second  half of the pattern by  setting the range from n-1 (we are using n-1 to remove the same line )
for i in range(n-1,0,-1):
    
    print("*"*i+" "*(n-i)+" "*(n-i)+"*"*i)     