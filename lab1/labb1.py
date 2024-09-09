##Write a program that takes two numbers from the user, adds them together, and prints the results. Make sure to handle the case where the user inputs strings instead of numbers (use int() to convert)
print('n1= ')
n1 = int(input())
print('n2= ')
n2 = int(input())
print(f"n1= {n1}  n2= {n2}" )

add = n1 + n2
print(f"Sum= {add}")


##Write a function convert_to_colsius(fahrenheit) that converts a temperature from Fahrenheit to Celsius using the formula:
#celsius = (Fahrenheit-32) * 5/9

def convert_to_colsius(fahrenheit):
     celsius = (fahrenheit - 32) * 5 / 9
     return celsius

print(convert_to_colsius((20)))



#   Write a program that takes a list of numbers and prints only the even numbers from the list.
listOfNumbers = [1,2,3,4,5,6,7,8,9]

for i in listOfNumbers:
    if(i%2 == 0):
        print(i)