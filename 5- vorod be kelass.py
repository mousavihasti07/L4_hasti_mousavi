name_list = ['a','s','d','f','g']

name = input('enter your name: ').lower().strip()
password = input('enter password: ').lower().strip()

if name not in name_list:
    print('karbar yaft nashod')
elif password == 'python123':
    print('khosh amadid')
else :
    print('')











