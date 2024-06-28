from collections import Counter

text = "hello world hello"
word_counts = Counter(text.split())
print("Frequency of words:", word_counts)
