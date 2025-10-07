def smallest_change(arr):
    ans = 0
    n = len(arr)
    half_length = n // 2
    i = 0
    while i < half_length:
        j = n - i - 1
        if arr[i] != arr[j]:
            ans += 1
        i += 1
    return ans