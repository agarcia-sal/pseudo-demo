def smallest_change(arr):
    ans = 0
    length = len(arr)
    half_length = length // 2
    index = 0
    while index < half_length:
        left_element = arr[index]
        right_element = arr[length - index - 1]
        if left_element != right_element:
            ans += 1
        index += 1
    return ans