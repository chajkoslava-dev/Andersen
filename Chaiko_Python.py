###Subtask 1

print("Subtask 1:")
correctInput1=0      #Сounter for correct input
while correctInput1==0:
    try:
        number = int(input("Enter the integer: "))  #The program asks to input the integer
        correctInput1+=1    
    except ValueError:          # The program handles the error when the user entered the wrong datatype
        print("You've just inputted the wrong datatype")

if number>7:    #If the integer is greater than 7, then the program prints "Hello"
    print("Hello")

else:           #In other cases print "Goodbye"
    print("Goodbye")

print("\n")

###Subtask 2
print("Subtask 2:")
name=input("Enter any name:")   #The program asks to enter the name
name=name.lower()               #The program сonverts the inputted name to lowercase
if name=="john":                #If the converted to lowercase name equals "john" then print "Hello, John"
    print("Hello, John")
else:                           #In other cases print "There is no such name"
    print("There is no such name")

print("\n")

###Subtask 3
print("Subtask 3:")
correctInput2=0     #Сounter for correct input
while correctInput2==0:
    try:
        raw = input("Enter the list of integers, separated by commas: ") #The program asks to input the list of integers, and separate them using commas
        nums = {int(x.strip()) for x in raw.split(",")} # Here we convert the input of user to the set of integers, deleting spaces and dividing the input of the user into parts by commas
        correctInput2+=1
    except:     #Here the program handles the error when the user entered the wrong format of input
        print("The program can't understand your input! Can you input again, please?")

mulnums=set() # Here the program creates the new set which will contain in itself the numbers from the input of the user that are multiples of 3
for i in nums:#In this cycle the program checks each number inputted by the user by division on 3(if the number is a multiple of 3 then this number is added to the new set)
    if i%3==0:
        mulnums.add(i)

if mulnums:#Here the program  outputs the results of the subtask depending on fullness of the set "mulnums"
    print("Numbers that are multiples of 3: ",mulnums)
else:
    print("There are no numbers that are multiples of 3")





