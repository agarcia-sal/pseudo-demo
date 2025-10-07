def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    length = len(arr)
    start_index = length - k
    ans = [arr[start_index + i] for i in range(k)]
    return ans