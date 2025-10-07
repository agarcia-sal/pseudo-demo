def sort_array(array):
    if len(array) == 0:
        return []
    else:
        copy_array = []
        for index in range(len(array)):
            copy_array.append(array[index])
        sum_first_last = array[0] + array[len(array) - 1]
        remainder = sum_first_last % 2
        if remainder == 0:
            copy_array.sort(reverse=True)
            return copy_array
        else:
            copy_array.sort()
            return copy_array