"""
Insertion sort
--------------
- Insertion sort is a sorting algorithm that places unsorted element in it's suitable position in each iteration.
- or at the time of insertion of the element, the element is sorted (it keeps finding the suitalbe position of that element till the element is sorted).

- utility
    - there are few number of elements in the array.
    - there are few elements left to be sorted.
"""


def insertion_sort(unsorted_list: list) -> list:
    """
    return a sorted list

    Args:
        unsorted_list: list

    Return:
        list
    """
    for i in range(1, len(unsorted_list)):

        # separate key variable
        k = unsorted_list[i]
        j = i - 1

        while j >= 0 and k < unsorted_list[j]:
            unsorted_list[j + 1] = unsorted_list[j]

            # decrement the value of j
            j = j - 1

        # assigning the key value when there is no element less than key
        unsorted_list[j + 1] = k

    return unsorted_list


unsorted_list = [9, 5, 1, 4, 3, 87, 36]
sorted_list = insertion_sort(unsorted_list)
print(f"sorted list : {sorted_list}")
