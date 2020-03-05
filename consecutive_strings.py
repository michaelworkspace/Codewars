"""
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
"""

def longest_consec(strarr, k):
    longest = ""
    if len(strarr) == 0 or k > len(strarr) or k <= 0:
        return ""
    for i in range(len(strarr) - k + 1):
        long = strarr[i:i+k]
        long = ''.join(long)
        if len(long) > len(longest):
                longest = long
    return longest
