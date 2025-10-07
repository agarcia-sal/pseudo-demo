def smallest_change(arr):
    ans = 0
    n = len(arr)
    half_n = n // 2
    i = 0
    while i < half_n:
        j = n - i - 1
        if arr[i] != arr[j]:
            ans += 1
        i += 1
    return ans