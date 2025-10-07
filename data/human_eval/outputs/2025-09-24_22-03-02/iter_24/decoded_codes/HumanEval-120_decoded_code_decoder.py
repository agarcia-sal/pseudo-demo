def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = []
    arr_length = len(arr)
    start_index = arr_length - k
    for i in range(start_index, arr_length):
        ans.append(arr[i])
    return ans