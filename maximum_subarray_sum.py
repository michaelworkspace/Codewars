"""
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


from typing import List


def max_sequence_bruteforce(arr: List[int]) -> int:
    # Brute force solution time complexity O(n^3)
    if len(arr) == 0:
        return 0
    if all(num < 0 for num in arr):
        return 0
    max_sum = arr[0]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            max_sum = max(max_sum, sum(arr[i:j]))
    return max_sum


assert max_sequence_bruteforce([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def max_sequence(arr: List[int]) -> int:
    # Time complexity O(n)
    if len(arr) == 0:
        return 0
    if all(num < 0 for num in arr):
        return 0
    curr_sum = arr[0]
    max_sum = arr[0]
    for num in arr[1:]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def max_subarray(nums):
    # Kadane's Algorithm
    largest = -float("inf")
    current = 0
    for num in nums:
	    current += num
	    largest = max(current, largest)
	    current = max(current, 0)
    return largest
