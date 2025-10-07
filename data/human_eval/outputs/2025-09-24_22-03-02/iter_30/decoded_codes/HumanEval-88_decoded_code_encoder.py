def sort_array(array):
    if len(array) == 0:
        return [[]]
    else:
        sum_first_last = array[0] + array[-1]
        is_even = (sum_first_last % 2 == 0)
        copy_array = []
        for index in range(len(array)):
            copy_array.append(array[index])
        if is_even:
            for i in range(len(copy_array) - 1):
                for j in range(len(copy_array) - i - 1):
                    if copy_array[j] < copy_array[j + 1]:
                        temp = copy_array[j]
                        copy_array[j] = copy_array[j + 1]
                        copy_array[j + 1] = temp
        else:
            for i in range(len(copy_array) - 1):
                for j in range(len(copy_array) - i - 1):
                    if copy_array[j] > copy_array[j + 1]:
                        temp = copy_array[j]
                        copy_array[j] = copy_array[j + 1]
                        copy_array[j + 1] = temp
        return copy_array