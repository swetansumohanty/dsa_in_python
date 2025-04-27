"""
binary serching

- It is searching algorithm that perform seraching on a sorted list. 
"""


def binary_search(arr, item):
    """serach the item in the given array and return the index position of item"""

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == item:
            return f"item found at {mid}"

        if arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1

    return "item not found"


print(binary_search([1, 2, 3, 5, 7], 10))
