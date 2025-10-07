def sort_array(array):
    if len(array) == 0:
        return []
    else:
        sum_first_and_last = array[0] + array[len(array) - 1]
        is_even = (sum_first_and_last % 2) == 0
        copy_array = []
        for index in range(len(array)):
            copy_array.append(array[index])
        if is_even:
            copy_array.sort(reverse=True)
            return copy_array
        else:
            copy_array.sort()
            return copy_array