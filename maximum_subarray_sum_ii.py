"""
Take a look to the kata Maximum Subarray Sum https://www.codewars.com/kata/maximum-subarray-sum In that kata (if you solved it), you had to give the maximum value of the elements of all the subarrays.

In this kata, we have a similar task but you have to find the sub-array or sub-arrays having this maximum value for their corresponding sums of elements. The wanted function: Python and Ruby: find_subarr_maxsum()// Javascript: findSubarrMaxSum()

find_subarr_maxsum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == [[4, -1, 2, 1], 6]
If in the solution we have two or more arrays having the maximum sum value, the result will have an array of arrays in the corresponding order of the array, from left to right.

find_subarr_maxsum([4, -1, 2, 1, -40, 1, 2, -1, 4]) == [[[4, -1, 2, 1], [1, 2, -1, 4]], 6]  # From left to right [4, -1, 2, 1] appears in the array before than [1, 2, -1, 4].
If the array does not have any sub-array with a positive sum of its terms, the function will return [[], 0].

See more cases in the Example Test Cases Window. Enjoy it!

Thanks to smile67 (Matthias Metzger from Germany for his important observations in the javascript version)
"""

from typing import List


def find_subarr_maxsum(arr):
    # Brute force solution
    if len(arr) == 0:
        return 0
    if all(num < 0 for num in arr):
        return [[], 0]
    max_sum = arr[0]
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            max_sum = max(max_sum, sum(arr[i:j]))
            if sum(arr[i:j]) ==  max_sum:
                result.append(arr[i:j])
    result = [item for item in result if sum(item) == max_sum]
    if len(result) != 1:
        return [result] + [max_sum]
    else:
        return result + [max_sum]
