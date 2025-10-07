def sort_array(array):
    if len(array) == 0:
        return [None]
    sum_of_first_and_last = array[0] + array[-1]
    is_even_sum = (sum_of_first_and_last % 2) == 0
    copy_of_array = list(array)
    if is_even_sum:
        copy_of_array.sort(reverse=True)
    else:
        copy_of_array.sort()
    return copy_of_array