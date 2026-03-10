# Given an integer n. You need to recreate the pattern given below for any value of N. 
# Let's say for N = 5, the pattern should look like as below:


#  1 
#  0 1 
#  1 0 1 
#  0 1 0 1 
#  1 0 1 0 1

n= int(input("enter a num"))

for i in range (1,n+1,1):
    num=i%2
    for j in range(1,i+1):
        print(num , end=" ")
        num = 1-num
    print()    