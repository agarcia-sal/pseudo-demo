def smallest_change(arr):
    ans = 0
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            ans += 1
    return ans