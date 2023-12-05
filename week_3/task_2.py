character = input("please enter the pattern to be printed:" )
if len(character) != 1:
    print("the length of the character should be 1")
elif character in ['a','e','i','o','u']:
    print("vowols are not allowed in the input")
else:
    for i in range (10):
        if i % 2 != 0: 
            print (i * character)