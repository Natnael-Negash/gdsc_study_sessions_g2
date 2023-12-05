sum = 0
three = 0
five = 0
for number in range(1, 51):
    if number % 2 == 0:
        sum += number
        if number % 3 == 0:
            three += number
            print("three")
        elif number % 5 == 0:
            five += number
            print ("five")
        else:
            print(number)
    else:
        print(number)

print ("the total sum of even numbers:", sum)
print("Count of 'Three' replacements: ", three)
print("Count of 'Five' replacements: ", five)
        

""" print("\nTotal Sum of Even Numbers: ", sum)"""

