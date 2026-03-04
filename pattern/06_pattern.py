# creating a variable num initilizing num as intiger getting input from user
num =int(input("enter a num"))
# creating a for loop 
# 0 is beging range and num+1 is ending range
# inside the range()
# range(start, stop, step)
# num is start, 0 is stop , and -1 is step 
# it first minus num  ends at 0 as o is referd as stop
for i in range (num,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
       

