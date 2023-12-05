word = input("please enter the word to check")
reverse_word = word[::-1]
if reverse_word == word:
    print("the word "  +  word  +  " is a palindrome.")
else:
    print("the word " + word + " is not palindore,", end="\n" "because " + reverse_word + " is not equal to " + word)
