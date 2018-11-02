print("Numbers from 1 to 10")
number=int(input("Guess the number: "))
number1=4
i=1
if number>10:
    print("Number shoud be from 1 to 10")
while i<11:
    if number ==number1:
        print("Great! You did it!")
        break
    else:
        print("Try again ")
        number=int (input("Guess the number: "))
    i=i+1
