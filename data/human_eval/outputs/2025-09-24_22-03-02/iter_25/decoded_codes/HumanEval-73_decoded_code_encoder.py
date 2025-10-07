def smallest_change(arr):
    ans = 0
    length = len(arr)
    half_length = length // 2
    for i in range(half_length):
        left_element = arr[i]
        right_index = length - i - 1
        right_element = arr[right_index]
        if left_element != right_element:
            ans += 1
    return ans