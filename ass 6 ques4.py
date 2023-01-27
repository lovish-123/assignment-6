# to check whether the string entered is a pangram or not
n = str(input("enter the string : "))
def pangrams(n):
    alphabet = "abcdefghijklmnopqrstuv"
    for char in alphabet:
        if char not in n:
         return False
    return True
pangrams(n)

if (pangrams(n)==True):
    print("it is a pangram")
else:
    print("it is not a pangram")