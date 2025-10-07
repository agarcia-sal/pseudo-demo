def move_one_ball(arr):
    if arr == []:
        return True
    min_index = arr.index(min(arr))
    rotated = arr[min_index:] + arr[:min_index]
    return rotated == sorted(arr)