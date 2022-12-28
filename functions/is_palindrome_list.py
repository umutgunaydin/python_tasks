# Write a function named is_palindrome that takes a list composed of strings as argument
# and returns True if the list is a palindrome and returns False otherwise
def is_palindrome_list(lis):
    word = "".join(lis)
    return word == word[::-1]


print(is_palindrome_list(['mr', 'owl', 'ate', 'my', 'metal', 'worm']))
