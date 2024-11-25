print("/**Note:-Password must contain Uppercase,Lowerscase,Special symbols,numbers, more than 6 values and no spaces**/")
password = input("Enter your password: ")


def passcheck(password):
    new=0
    num =False
    for val in password:
        if val.isnumeric():
            num = True
            break             
    if len(password)>6 and len(password)<15:
        if password.upper():
            if password.lower():
                if not password.isalnum():
                    if num==True:
                        if password.__contains__(" ") == False:
                            print("Valid password")
                        else:
                            print("Invalid password!,  should not contain spaces")
                            new+=1
                    else:
                        print("Invalid password!,  should contain numbers")
                        new+=1 
                else:
                    print("Invalid password!,  should contain special symbols")
                    new+=1 
            else:
                print("Invalid password!,  should contain lowercase letters")
                new+=1    
        else:
            print("Invalid password!, should contain uppercase letters")
            new+=1    
    else:
        print("Invalid password! ,password length must be more than 6 values!")
        new+=1
    if new == 1:
        password = input("Enter new password: ")
        passcheck(password)
        
passcheck(password)
