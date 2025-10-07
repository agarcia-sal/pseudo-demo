def smallest_change(arr) -> int:
    ans = 0
    for index in range(len(arr) // 2):
        if arr[index] != arr[len(arr) - index - 1]:
            ans += 1
    return ans