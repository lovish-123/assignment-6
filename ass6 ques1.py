n = int(input("enter your number : "))

def perfect_numbers(n):
    i = 1
    while i < n:
        if n % i == 0:
            divisors.append(i)
        i = i + 1


    temp = 0
    for j in divisors:
       temp = temp +j

    if temp == n :
       print("It is a perfect number.")
    else :
        print("no")

perfect_numbers(n)
