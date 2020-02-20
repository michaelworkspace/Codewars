"""
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

"""

def first_non_repeating_letters(string):
    string_lower = string.lower()
    for index, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[index]
    return ""

##def first_non_repeating_letter(string):
##    if not string:
##        return ''
##    
##    dict = {}
##    lowercase_string = string.lower()
##    
##    # first we have to make a dictionary counting how many occurrences there are
##    for ch in lowercase_string:
##        if ch in dict:
##            dict[ch] = dict[ch] + 1
##        else:
##            dict[ch] = 1
##            
##    # check if the number of occurrences is one, then return it
##    for ch in lowercase_string:
##        if ch in dict and dict[ch] == 1:
##            index = lowercase_string.find(ch)
##            return string[index]
##            
##    for count in dict.values():
##        if count != 1:
##            return ''
