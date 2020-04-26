"""
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""



def expanded_form(num):
    num = str(num)
    ans = ''
    for x in num:
        if x == "0":
            num = num[:-1]
        else:
            ans += x + "0" * (len(num)-1) + ' + '
            num = num[:-1]
    return ans[:-3]
