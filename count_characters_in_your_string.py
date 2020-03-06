"""
The main idea is to count all the occurring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }

For C#: Use a Dictionary<char, int> for this kata!
"""

from collections import Counter


def count(string):

# Traditional approach using dictionary
#     d = {}
#     for char in set(string):
#         d[char] = string.count(char)
#     return d
#
# Using the collections.Counter approach

    return Counter(string)
