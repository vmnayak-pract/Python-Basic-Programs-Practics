# This program will be able to check for palindrome of string and number both type of data.

user_inp = input("Enter a input to check for palindrome: ")

if user_inp == user_inp[::-1]:
    print("Your input \""+ user_inp+"\" is palindrome.")
else:
    print("Not Palindrome")
