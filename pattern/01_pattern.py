#Given an integer n. You need to recreate the pattern given below for any value of N
# . Let's say for N = 5, the pattern should look like as below:



#*****
#*****
#*****
#*****
#*****

#creating a variable n initilizing n as intiger getting input from user  
n=int(input("enter a num"))
#creating a for loop i as beginning range and n as end of range
for i in range (n):
#using print function to print "*"  and multiplying it with n  
    print("*"*n)