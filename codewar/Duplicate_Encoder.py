# The goal of this exercise is to convert a string to a new string where each character in the new string is
# "(" if that character appears only once in the original string, or ")" if that character appears more than once in
# the original string. Ignore capitalization when determining if a character is a duplicate.

def duplicate_encode(word):
    # your code here
    word = word.lower()
    result = ''
    for i in word:
        numOfLetter = word.count(i)
        if numOfLetter > 1:
            result = result + ')'
        else:
            result = result + '('
    return result


case = duplicate_encode('word')
print(case)

# Best practice     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])