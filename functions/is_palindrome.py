# Write a function named is_palindrome that takes a string as argument
# and returns True if the string is a palindrome
# and returns False otherwise
def is_palindrome(word):
    return word == word[::-1]


print(is_palindrome("neveroddoreven"))
