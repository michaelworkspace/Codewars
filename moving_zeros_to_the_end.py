"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array):
    count_zeros = 0
    ans = []
    for i in range(len(array)):
        if array[i] == 0 and type(array[i]) == int or type(array[i]) == float:
            count_zeros += 1
        else:
            ans.append(array[i])
    ans.extend([0] * count_zeros)
    return ans
