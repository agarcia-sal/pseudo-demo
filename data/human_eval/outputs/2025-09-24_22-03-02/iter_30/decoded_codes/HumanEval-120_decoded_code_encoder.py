def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = []
    length_arr = len(arr)
    start_index = length_arr - k
    index = start_index
    while index < length_arr:
        ans.append(arr[index])
        index += 1
    return ans