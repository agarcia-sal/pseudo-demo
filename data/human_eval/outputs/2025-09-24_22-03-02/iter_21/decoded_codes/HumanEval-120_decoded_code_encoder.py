def maximum(arr: list, k: int) -> list:
    if k == 0:
        return []
    arr.sort()
    ans = []
    start_index = len(arr) - k
    end_index = len(arr) - 1
    for index in range(start_index, end_index + 1):
        ans.append(arr[index])
    return ans