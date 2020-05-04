"""
Given a 2D list of size m * n. Your task is to find the sum of minimum value in each row.

For Example:

[
  [1, 2, 3, 4, 5],       # minimum value of row is 1
  [5, 6, 7, 8, 9],       # minimum value of row is 5
  [20, 21, 34, 56, 100]  # minimum value of row is 20
]
So, the function should return 26 because sum of minimums is as 1 + 5 + 20 = 26

Note: You will be always given non-empty list containing Positive values.
"""


from typing import List



def sum_of_minimums(numbers: List[int]) -> int:
##    # Traditional approach
##    res = 0
##    for item in numbers:
##        res += min(item)
##    return res

    # One-liner
    return sum(min(rows) for rows in numbers)
