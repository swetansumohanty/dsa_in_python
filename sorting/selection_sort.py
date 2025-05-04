"""
selection sort
--------------

- selection sort is a sorting algorithm it search for smallest element in each iteration of the unsorted list and
  place that element in the beginning of the list.

- utility
    - a small list to be sorted
    - cost of swapping doesn't matter
    - checking all items in the list is compulsory
"""


def selection_sort(unordered_list: list) -> list:
    """
    returns a sorted list

    Args:
        unordered_list: list

    Returns:
        list
    """

    # loops through each item of the element
    for i in range(len(unordered_list)):

        # setting first index as smallest element
        min_index = i

        # loops to comparing elements
        for j in range(i + 1, len(unordered_list)):

            if unordered_list[j] < unordered_list[min_index]:
                min_index = j

        unordered_list[i], unordered_list[min_index] = (
            unordered_list[min_index],
            unordered_list[i],
        )

    return unordered_list


unordered_list = [-2, 45, 0, 11, -9]
ordered_list = selection_sort(unordered_list)
print(f"ordered list: {ordered_list}")
