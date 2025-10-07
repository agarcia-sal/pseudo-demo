def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = []
    arr_length = len(arr)
    start_index = arr_length - k
    end_index = arr_length - 1
    for i in range(start_index, end_index + 1):
        ans.append(arr[i])
    return ans