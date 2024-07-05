def longest_word(string):
    words = string.split()
    return max(words, key=len)

string = "Find the longest word in this string"
print("The longest word is", longest_word(string))
