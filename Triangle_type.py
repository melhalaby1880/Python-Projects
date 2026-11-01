print ( "Welcome to the triangle app" )
x = float ( input ( "Please enter the first side : " ) ) # first side = x 
y = float ( input ( "Please enter the second side : " ) ) # second side = y 
z = float ( input ( "Please enter the third side : " ) ) # third side = z 
if x > 0 and y > 0 and z > 0 :
    if ( x + y ) > z and ( x + z ) > y and ( y + z ) > x :
        if x == y == z :
            print ( "This is an equilateral triangle" )
        elif x == y or x == z or y == z:
            print ( "This is an isosceles triangle" )
        else :
            print ( "This is a Scalene Triangle ")
    else :
        print ( "These sides cannot form a triangle" )
else :
    print ( "Please enter positive side lengths" )