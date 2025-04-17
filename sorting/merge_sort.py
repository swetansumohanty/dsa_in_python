"""
merge sort
----------

- merge sort is a popular sorting algorithm which is based upon devide and conquer algorithm.
- mearge sort take a list , devide into sub lists and merge the sub lists to get the sorted list.

"""


def merge_sort(unsorted_list: list):
    """sort the list"""

    # first check the length of the given list should be greater than zero
    if len(unsorted_list) > 1:

        # find mid
        mid = len(unsorted_list) // 2

        # create sub lists
        left_list = unsorted_list[:mid]
        right_list = unsorted_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0

        while (i < len(left_list)) and (j < len(right_list)):
            if left_list[i] < right_list[j]:
                unsorted_list[k] = left_list[i]
                i += 1
            else:
                unsorted_list[k] = right_list[j]
                j += 1

            k += 1

        while i < len(left_list):
            unsorted_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            unsorted_list[k] = right_list[j]
            j += 1
            k += 1


unsorted_list = [6, 5, 12, 10, 9, 1]
merge_sort(unsorted_list)
print(unsorted_list)
