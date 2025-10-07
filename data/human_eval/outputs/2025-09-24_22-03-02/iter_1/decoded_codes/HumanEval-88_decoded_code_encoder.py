def sort_array(arr):
    if not arr:
        return []
    rev = ((arr[0] + arr[-1]) % 2 == 0)
    return sorted(arr, reverse=rev)