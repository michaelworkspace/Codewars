"""
Sam is an avid collector of numbers. Every time he finds a new number he throws it on the top of his number-pile. Help Sam organise his collection so he can take it to the International Number Collectors Conference in Cologne.

Given an array of numbers, your function should return an array of arrays, where each subarray contains all the duplicates of a particular number. Subarrays should be in the same order as the first occurence of the number they contain:

group([3, 2, 6, 2, 1, 3])
>>> [[3, 3], [2, 2], [6], [1]]
Assume the input is always going to be an array of numbers. If the input is an empty array, an empty array should be returned.
"""


from typing import List
from collections import Counter


def group(arr: List[int]) -> List[List[int]]:
    # collections.Counter Approach
    arr_count = Counter(arr)

# Dictionary approach
#     arr_count = {}
#     for num in arr:
#         arr_count[num] = arr.count(num)

    res = [[key] * value for key, value in arr_count.items()]

    return res
