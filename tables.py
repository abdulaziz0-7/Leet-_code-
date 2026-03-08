# Write a program to print the multiplication table of a given number up to a specified limit.
# firstwe get  table and times as user input and conver it into integer using int( function )
table= int (input("enter table:"))
times= int(input("enter times:"))
#creating a for loop in which we start the loop from 0 , stop  loop at times and step as 1 
for i in range(0,times+1,1):
# then print table * i for each iteration of loop     
    print(table*i)