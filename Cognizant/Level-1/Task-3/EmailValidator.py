mail = input("Enter your email address : ")
i=0
if ("@" in mail) and (mail.count("@")==1) and ((mail[-5]=="@")==False):
    if (" " in mail)==False:
        if mail[-4]=="." or mail[-3]==".":
            for value in mail:
                if value.isalpha():
                    if value == value.upper():
                        i+=1
                        break
                break
            if i==0:
                print("Valid email address.")
            else:
                print("Invalid email address!")
else:
    print("Invalid email address!")
    