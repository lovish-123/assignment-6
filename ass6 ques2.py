# finding a palindrome
n = str(input("enter your word or phrase : "))
def function1(n):
    i = len(n)-1
    b = ""
    while i>=0:
        b=b+n[i]
        i-=1
    print(b)
    if b == n:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")

function1(n)

