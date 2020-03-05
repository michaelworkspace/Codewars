"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""


def sort_array(source_array):
    sorted_odds = []
    even_numbers_indexed = []
    for index, number in enumerate(source_array):
        if number % 2 == 1:
            sorted_odds.append(number)
        else:
            even_numbers_indexed.append((index, number))
    sorted_odds.sort()
    for item in even_numbers_indexed:
        sorted_odds.insert(item[0], item[1])
    return sorted_odds
