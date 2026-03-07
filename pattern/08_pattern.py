# Given an integer n. You need to recreate the pattern given below for any value of N.
#  Let's say for N = 5, the pattern should look like as below:

#     *
#    ***
#   *****
#  *******
# *********

#first get usre input uing input and convert using int()
n = int(input("Enter n: "))

#create a loop starts from n , stops before 0   and -1 as step
for i in range(n, 0,-1):
# print space by multiplying the empty string ,for example user input =5 , 5-i = 4 so empty string * 4 ="    " 
# print    "*" * (2*1-1)= 1 so it will print 1* "*"= *
# then using + concantation we add spaces and "* together"
    print(" " * (n - i)  +  "*" * (2 * i - 1))