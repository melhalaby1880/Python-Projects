print ( "welcome to our calculator app" .capitalize () )
num1 = float ( input ( "enter the first number : " . capitalize () ) ) 
symbol = input ( "enter an operation ( + , - , * , / , % ) : " )
num2 = float ( input ( "enter the second number : " . capitalize () ) )
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
    print ( "wrong operation " + str ( symbol ) )
