print ( "Welcome to our calculator app" )
num1 = float ( input ( "Enter the first number : " ) ) 
symbol = input ( "Enter an operation ( + , - , * , / , % ) : " )
num2 = float ( input ( "Enter the second number : " ) )
if symbol == "+" :
    print ( str ( num1 ) + ' + ' + str ( num2 ) + ' = ' + str ( num1 + num2 ) )
elif symbol == "-" :
    print ( str ( num1 ) + ' - ' + str ( num2 ) + ' = ' + str ( num1 - num2 ) )
elif symbol == '*' :
    print ( str ( num1 ) + ' * ' + str ( num2 ) + ' = ' + str ( num1 * num2 ) )
elif symbol == '/' :
    if num2 == 0 :
        print ( "It cannot be divided by 0 " )
    else :
        print ( str ( num1 ) + ' / ' + str ( num2 ) + ' = ' + str ( num1 / num2 ) )
elif symbol == '%' :
    print ( str ( num1 ) + ' % ' + str ( num2 ) + ' = ' + str ( num1 % num2 ) )
else : 
    print ( "Wrong operation " + str ( symbol ) )
