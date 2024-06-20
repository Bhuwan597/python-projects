email = input('Type the email: ')
k=0
j=0
l=0
if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@') == 1):
            if (email[-4] == '.') ^ (email[-3] == '.'):
                for character in email:
                    if character.isspace():
                        k=1
                    elif character.isalpha():
                        if character == character.upper():
                            j=1
                    elif character.isdigit():
                        continue
                    elif character == '_' or character=='@' or character == '.':
                        continue
                    else:
                        l = 1 
                if k ==1 or j ==1 or l==1:
                    print('Wrong Email 5')
            else:
                print('Wrong Email 4')
        else:
            print('Wrong Email 3')
    else:
        print('Wrong Email 2')
else:
    print('Wrong Email 1')