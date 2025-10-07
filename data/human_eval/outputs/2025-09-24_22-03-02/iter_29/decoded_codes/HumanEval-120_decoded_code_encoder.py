def maximum(arr: list[int], k: int) -> list[int]:
    if k == 0:
        return []
    arr.sort()
    ans = []
    for index in range(len(arr) - k, len(arr)):
        ans.append(arr[index])
    return ans