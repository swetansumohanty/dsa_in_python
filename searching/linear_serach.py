"""linear search"""


def linear_search(arr, item):
    """
    serch the item in linear fashion

    Args:
        arr: array
        item: searching item

    Returns:
        index positon of the item found at
    """

    for i in range(len(arr)):
        if arr[i] == item:
            return i

    else:
        return f"item {item} not found"


print(linear_search([9, 3, 23, 84, 67, 5, 8], 9))
