def smallest_change(arr):
    ans = 0
    n = len(arr)
    half_length = n // 2
    i = 0
    while i < half_length:
        if arr[i] != arr[n - i - 1]:
            ans += 1
        i += 1
    return ans