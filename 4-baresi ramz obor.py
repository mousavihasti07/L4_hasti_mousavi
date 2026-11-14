#_________________________________________________________1:
  


password = input('enter password:')

if len(password) < 8:
    print('ramz kotah')
    
if password.isdigit():
    print('ramz faghat adad ast')
    
if ' ' in password:
    print('ramz daraye faseleh ast')
    
    
    
#________________________________________________________2:

password = input('enter password:')



if len(password) > 8:
    if not password.isdigit():
      
        if not ' ' in password:
           print('ramz moafagh') 
        else:
            print('ramz daraye faseleh ast')  
    else:
        print('ramz faghat adad ast')
else:
    print('ramz kotah')


#______________________________________________3:
    
password = input('enter password:')

if len(password) < 8:
    print('ramz kotah')
elif password.isdigit():
    print('ramz faghat adad ast')
elif ' ' in password:
    print('ramz daraye faseleh ast') 
else:
    print('ramz moafagh')















