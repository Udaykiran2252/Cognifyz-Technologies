string = input("Enter the String: ")
reverse = ""

for i in string:
    reverse = i + reverse
    
if string == reverse:
    print("Given string is a Palindrome")
else:
    print("Given string is not a Palindrome")