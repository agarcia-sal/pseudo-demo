def smallest_change(arr):
    ans = 0
    n = len(arr)
    half_length = n // 2
    for i in range(half_length):
        left_element = arr[i]
        right_element = arr[n - i - 1]
        if left_element != right_element:
            ans += 1
    return ans