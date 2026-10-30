print ( "hello this is a proggram to know which number is the greatest" .capitalize () )
num1 = float ( input ( "enter the first number : " . capitalize () ) )
num2 = float ( input ( "enter the second number : " . capitalize () ) )
num3 = float ( input ( "enter the third number : " . capitalize () ) )
greatest_num = num1 
if ( num2 > greatest_num ) :
    greatest_num = num2
if ( num3 > greatest_num ) :
    greatest_num = num3
print ( "the greatest number you've entered is : " . capitalize () + str ( greatest_num ) )