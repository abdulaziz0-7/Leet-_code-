# Given an integer n. You need to recreate the pattern given below for any value of N.
# Let's say for N = 5, the pattern should look like as below:


# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

# create a variable n to store user input ,using int to store it as integer and using input function  to get input from user
n= int(input("enter a num"))

# creating a variable num which holds 1  
num=1

# creating a for loop which start from 1 , ends befor n+1 and 1 as step 
for i in range (1,n+1,1):
    for j in range(1,i+1):
        print(num , end=" ")
        num = num+1
    print()    