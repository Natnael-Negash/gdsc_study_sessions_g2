# week two project  Word Frequency Analyzer

# Task - 1: Input Text
"""ask users to enter a paragraph of text and store it in
a variable called paragraph for further processing"""

def input_text():
    paragraph = input("Enter a paragraph of paragraph: ")
    return paragraph

# Task - 2: Word Tokenization
"""take the input paragraph and splits it into
individual words and storing them in a list"""

def word_tokenization(paragraph):
    words = paragraph.split()
    return words

# Task - 3: Word Frequency Calculation
""" counts the frequenc of each word in the paragraph and
store the word in frequencies in a dictionary"""

def word_frequency_calculation(words):
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

# Task - 4: Display Word Frequencies
""" displays the word frequencies in descending order,
 printing the word and its corresponding frequency. """
def display_word_frequencies(word_frequency):
    sorted_word_freq = {k: v for k, v in sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)}
    for word, freq in sorted_word_freq.items():
        print(f"{word}: {freq}")

# Task - 5: Top N Words
""" modifies the function from Task 4 to display only the top N most
 frequent words, prompting the user to enter the value of N. """
def top_n_words(word_frequency, n):
    sorted_word_freq = {k: v for k, v in sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)}
    top_n = dict(list(sorted_word_freq.items())[:n])
    for word, freq in top_n.items():
        print(f"{word}: {freq}")

# Task - 6: Word Search
"""- prompts the user to enter a word and searches for it in the text,
 displaying the frequency of the word if it is found. If the word is
   not present, it displays a suitable message."""
def word_search(word_frequency, word):
    if word in word_frequency:
        print(f"The word '{word}' appears {word_frequency[word]} times.")
    else:
        print(f"The word '{word}' is not found in the paragraph.")


text = input_text()
words = word_tokenization(text)
word_frequency = word_frequency_calculation(words)
display_word_frequencies(word_frequency)
search_for_word = input("Enter a word to search for: ")
word_search(search_for_word, word_frequency)

