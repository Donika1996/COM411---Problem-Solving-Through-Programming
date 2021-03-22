#WHILE loop to print a countdown of numbers, froma a user defined value e.g. if user gives me 5, my code will print 5,4,3,2,1 BOOM

print("What is the starting point?")
start = int(input()) #control variable/counter
start_copy = start


while(start>=1): #condition that needs to be satisfied for loop to continue
 print(start)
 start-=1 #Start =0
print("BOOM!!!")





for counter in range(start, 0, -1):
  print(counter)
print("BOOM!!!")