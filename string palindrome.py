# WAP to take a string as input and check if palindrome or not.

s=input("Enter a string:")
s1=s[::-1]
if s==s1:
    print("Palindrome.")
else:
    print("Not a Palindrome.")