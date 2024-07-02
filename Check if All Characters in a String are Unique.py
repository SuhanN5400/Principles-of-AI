def all_unique_characters(string):
    return len(string) == len(set(string))

string = "abcdef"
if all_unique_characters(string):
    print(string, "has all unique characters")
else:
    print(string, "does not have all unique characters")
