def smallest_change(array_of_integers):
    change_count = 0
    length = len(array_of_integers)
    for index in range(length // 2):
        if array_of_integers[index] != array_of_integers[length - index - 1]:
            change_count += 1
    return change_count