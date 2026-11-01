print ( "| Welcome to grades app |" )
grade = float ( input ( "Please enter your grade : " ) )
if grade >= 0 and grade <= 100 :
    if grade >= 90 :
        if grade > 95 :
            print ( "A+" )
        else :
            print ( "A" )
    elif grade >= 80 :
        print ( "A-" )
    elif grade >= 70 :
        print ( "B" )
    elif grade >= 60 :
        print ( "C" )
    elif grade >= 50 :
        print ( "D" )    
    else : 
        print ( "F" )
else :
    print ( "Try again and please enter a grade between 0 and 100 " )