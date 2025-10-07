def smallest_change(arr) -> int:
    ans = 0
    length_of_arr = len(arr)
    half_length = length_of_arr // 2
    for i in range(half_length):
        left_element = arr[i]
        right_element = arr[length_of_arr - i - 1]
        if left_element != right_element:
            ans += 1
    return ans