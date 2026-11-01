print ( "Hello this is a proggram to know which number is the greatest" )
num1 = float ( input ( "Enter the first number : " ) )
num2 = float ( input ( "Enter the second number : " ) )
num3 = float ( input ( "Enter the third number : " ) )
greatest_num = num1 
if num2 > greatest_num :
    greatest_num = num2
if num3 > greatest_num :
    greatest_num = num3
print ( "The greatest number you've entered is : " + str ( greatest_num ) )