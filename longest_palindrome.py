"""
Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""

def longest_palindrome(s: str) -> int:
    # Traditional approach with nested for loops
    #     ans = 0
    #     for i in range(len(s)):
    #         for j in range(i+1, len(s)+1):
    #             if s[i:j] == s[i:j][::-1]:
    #                 ans = max(len(s[i:j]), ans)
    #
    # One-liner approach
    return 0 if not s else max(len(s[i:j]) for i in range(len(s)) for j in range(i+1, len(s)+1) if s[i:j] == s[i:j][::-1])
