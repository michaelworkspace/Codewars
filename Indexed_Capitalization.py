"""
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
The input will be a lowercase string with no spaces and an array of digits.

Good luck!

Be sure to also try:

Alternate capitalization

String array revisal
"""
def capitalize(s,ind):
# Traditional Method
#
#     res = ""
#     for i in range(len(s)):
#         if i in ind:
#             res += s[i].upper()
#         else:
#             res += s[i]
#     return res
#
## One-Liner Method
    return "".join(s[i].upper() if i in ind else s[i] for i in range(len(s)))
