def sort_array(array):
    if len(array) == 0:
        return []
    else:
        sum_first_last = array[0] + array[-1]
        is_reverse = (sum_first_last % 2 == 0)
        copy_array = list(array)
        n = len(copy_array)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if is_reverse:
                    if copy_array[j] < copy_array[j + 1]:
                        copy_array[j], copy_array[j + 1] = copy_array[j + 1], copy_array[j]
                else:
                    if copy_array[j] > copy_array[j + 1]:
                        copy_array[j], copy_array[j + 1] = copy_array[j + 1], copy_array[j]
        return copy_array