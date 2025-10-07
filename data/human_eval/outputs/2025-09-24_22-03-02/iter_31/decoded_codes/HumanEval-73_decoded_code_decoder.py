def smallest_change(arr):
    ans = 0
    n = len(arr)
    half_length = n // 2
    for i in range(half_length):
        if arr[i] != arr[n - i - 1]:
            ans += 1
    return ans