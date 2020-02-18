"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""


def zeros(n):
      
    # Initialize result 
    count = 0
  
    # Keep dividing n by 
    # powers of 5 and 
    # update Count 
    i=5
    while (n/i>=1): 
        count += int(n/i) 
        i *= 5
  
    return int(count) 

## Naive approach
#
#     fact = 1
#     trailing_zeros = 0
#     for i in range(1, n+1):
#         fact *= i
#     fact = str(fact)
#     for i in fact[::-1]:
#         if i == '0':
#             trailing_zeros += 1
#         else:
#             break
#     return trailing_zeros
