""" Write a Python program to find and print
the sum of all the even numbers from 1 to 50 (inclusive).
Additionally, for each even number, if it is a multiple of 3,
print "Three" instead of the number; if it is a multiple of 5,
 print "Five" instead of the number. Finally, print the total
   sum and the count of numbers replaced with "Three" or "Five." """

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
        

