def smallest_change(arr: list[int]) -> int:
    ans = 0
    length = len(arr)
    half_length = length // 2
    for i in range(half_length):
        if arr[i] != arr[length - i - 1]:
            ans += 1
    return ans