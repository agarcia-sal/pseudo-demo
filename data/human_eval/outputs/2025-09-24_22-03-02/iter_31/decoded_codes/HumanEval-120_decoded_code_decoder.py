def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = []
    length_arr = len(arr)
    start_index = length_arr - k
    end_index = length_arr - 1
    for i in range(start_index, end_index + 1):
        ans.append(arr[i])
    return ans