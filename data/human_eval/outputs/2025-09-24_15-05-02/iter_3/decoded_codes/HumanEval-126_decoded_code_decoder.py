def is_sorted(lst):
    # Count occurrences of each element in the list
    count_digit = {key: 0 for key in lst}
    for i in lst:
        count_digit[i] += 1

    # Check if any element appears more than twice
    for count in count_digit.values():
        if count > 2:
            return False

    # Check if the list is sorted in non-decreasing order
    for index in range(1, len(lst)):
        if lst[index - 1] > lst[index]:
            return False

    return True