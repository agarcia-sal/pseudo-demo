def smallest_change(arr) -> int:
    ans = 0
    n = len(arr)
    for index in range(n // 2):
        if arr[index] != arr[n - index - 1]:
            ans += 1
    return ans