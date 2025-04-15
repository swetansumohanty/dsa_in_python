"""
bubble sort
-----------
- buuble sort is a sorting algorithm where it compares two adjacent elements and swaps them until they are in intended order.

- utility
    - complexity doesn't matter
    - short and simple code is prefered
"""


def bubble_sort(unordered_list: list) -> list:
    """
    returns a sorted list

    Args:
        unordered_list: list

    Returns:
        list
    """

    # loops through each item of the list
    for i in range(len(unordered_list)):

        # loops to compare adjacent elements in a list
        for j in range(0, len(unordered_list) - i - 1):

            # check element is greater or not
            if unordered_list[j] > unordered_list[j + 1]:

                # swap the elements
                unordered_list[j], unordered_list[j + 1] = (
                    unordered_list[j + 1],
                    unordered_list[j],
                )
                # print("item swapped")

    return unordered_list


unordered_list = [-2, 45, 0, 11, -9]
sorted_list = bubble_sort(unordered_list)

print(f"sorted list : {sorted_list}")
