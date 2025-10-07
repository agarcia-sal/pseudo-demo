def sort_array(array):
    length = len(array)
    if length == 0:
        return []
    else:
        first_value = array[0]
        last_value = array[length - 1]
        sum_first_last = first_value + last_value
        remainder = sum_first_last % 2
        reverse_flag = remainder == 0
        array_copy = [array[i] for i in range(length)]
        array_copy.sort(reverse=reverse_flag)
        return array_copy