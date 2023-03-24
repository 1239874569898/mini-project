def display_menu():
    print('''Menu items:
    enter 1 to sign in
    enter 2 to sign up:''')


def user1():
    name = print(input('please enter your user name: '))
    password = print(input('please enter your password: '))
    return name, password

def user2():
    email = print(input('please enter your user email: '))
    password = print(input('please enter your password: '))
    return email, password



import re
def validate_password(password):
    if (len(password)< 8):
        return False
        print('please try again, password should be more than 8 characters, include numbers and letters.')
    elif ( not re.search('[0-9]',password)):
        return False
        print('please try again, password should be more than 8 characters, include numbers and letters.')
    elif( not re.search('[A-Z]',password)):
        return False
        print('please try again, password should be more than 8 characters, include numbers and letters.')
    elif( not re.search('[a-z]',password)):
        return False
        print('please try again, password should be more than 8 characters, include numbers and letters.')
    else:
        return True
    
  
emaillist = ['aaa@hotmail.com', 'bbb@gmail.com', 'ccc@icloud.com']
passwordlist = ['!@AE123tyuh', 'hjaIOhf1456-*/', ')(*fskjRT4665']

time = 0

display_menu()
num = int(input('please enter the number:'))
if num == 1:
    password = user1()
    validate_password(password)
    if(True):
        print('welcome! You were successful in joining.')
if num == 2:
    email, password = user2()
    while email not in emaillist and password not in passwordlist and time < 3:
        user2()
        if password in passwordlist and email in emaillist:
            print('welcome')
        elif time == 3:
            break
        else:
            print('Try again.')
            time += 1


    




    







