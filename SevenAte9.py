"""
Write a function that removes every lone 9 that is inbetween 7s.

seven_ate9('79712312') => '7712312'
seven_ate9('79797') => '777'
Input: String Output: String
"""
def seven_ate9(str_):
# Traditional Method
#     res = ""
#     for i in range(len(str_)-1):
#         if str_[i] == "9" and str_[i-1] == "7" and str_[i+1] == "7":
#             continue
#         else:
#             res += str_[i]
#     return res + str_[-1]
#
# One-Liner Method
    return ''.join('' if str_[i] == "9" and str_[i-1] == "7" and str_[i+1] == "7" else str_[i] for i in range(len(str_)-1)) + str_[-1]
