def move_one_ball(arr) -> bool:
    if len(arr) == 0:
        return True

    sorted_array = sorted(arr)

    min_value = min(arr)

    min_index = arr.index(min_value)

    my_arr = []
    for index in range(min_index, len(arr)):
        my_arr.append(arr[index])
    for index in range(0, min_index):
        my_arr.append(arr[index])

    for i in range(len(arr)):
        if my_arr[i] != sorted_array[i]:
            return False

    return True