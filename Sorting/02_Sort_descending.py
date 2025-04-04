# Sort Descending
# The .sort() method also accepts some optional parameters. This is the .sort() function signature:
# def sort(key=None, reverse=False) -> None:
# The key parameter allows us to customize the sorting order. We will learn more about this soon.
# The reverse parameter is a boolean value that determines whether the list should be sorted in descending order. By default, it is set to False.
# If we want to sort a list in descending order, we can set the reverse parameter to True.
# elements = [5, 3, 6, 2, 1]
# elements.sort(key=None, reverse=True)
# print(elements) # [6, 5, 3, 2, 1]

from typing import List


def sort_words(words: List[str]) -> List[str]:
    words.sort(reverse=True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(reverse=True)
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    numbers.sort(reverse=True)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))









# We can actually omit the key parameter and only pass the reverse parameter, by using a feature of Python called keyword arguments.

# elements.sort(reverse=True)
# It's also possible for us to sort the list in ascending order and then manually reverse the result.

# elements = [5, 3, 6, 2, 1]

# elements.sort()

# elements.reverse()