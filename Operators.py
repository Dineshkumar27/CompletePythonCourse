#to make a line into comment, select the line and press ctrl+/



#1.Arithmetic Operators
#Addition -> +
#Subtraction -> -
#Multiplication -> *
#Division -> /
#Floor Division (Quotient only) -> //
#Modulo(Only Reminder) -> %
#Exponential (Power of a number)-> **

# number1=10
# number2=3
# print("Addition",number1+number2)#13
# print("Subtraction",number1-number2)#7
# print("Multiplication",number1*number2)#30
# print("Division ", number1/number2)#3.3333
# print("Floor Division(only quotient)",number1//number2)#3
# print('Modulo (only remainder)',number1%number2)#1
# print('Exponential(power of a number)',number1**number2)#1000


#I am fixing an alarm clock to ring after 50Hrs from now, at what time it rings?
# bignumber%smallnumber--> remaining number Eg:50%24=2
# smallnumber%bignumber--> smallnumber Eg;6%10=6
# timeNow=10
# alarmSethours=50
# hoursPerday=12
# remainingTime=alarmSethours%hoursPerday
# alarmRings=timeNow+remainingTime
# print("Alarm ticks at", alarmRings)

#Case2: Sum of digits 64=10, 77=14,11=2
#Which number should I used to get 6 as quotient and 4 as remainder? 10

# inputNumber=4
# divisor=10
# quotient=inputNumber//divisor #2
# remainder=inputNumber%divisor #4
# result=quotient+remainder
# print("Result:",result)

#how to get input from the user

# userInput=input("Enter you input")#all will be string
# print(type(userInput))


#to convert userinput into int or float

# userInput=int(input("Enter your number"))
# print(type(userInput))
#
# print(userInput+1)

#to convert the input into your preferred datatype
# userInput=eval(input("Enter your number"))
# print(type(userInput))
#
# #expression any line with operators
# #eg. 10+9,10>20
# print(eval('9+8'))

#if express has more than one operator it uses PEMDAS(paranthesis,Exponentiation,Multiply,Divide,Addition,Subtract)
# 5+9*4+3/2
# 5+36+3/2
# 5+36+1.5
# # 42.5
#
# userInput=5+9.3*4+3/2;
# print(userInput)


#2.Assignment Operator(=,+=,-=,*=,/+,//=,%=)
# used to update the value

number=10 #assinging 10 value to number variable
print("Before Increment",number)
number=number+1 #11
number+=1#add the value 1 with current value of number and update the number
print("After Increment",number)


print()
numberinput=9;
number-=1
print(number)








