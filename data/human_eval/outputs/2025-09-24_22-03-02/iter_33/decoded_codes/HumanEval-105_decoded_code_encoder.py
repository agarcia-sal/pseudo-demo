def by_length(arr):
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    filtered_arr = [x for x in arr if 1 <= x <= 9]
    sorted_arr = sorted(filtered_arr, reverse=False)
    sorted_arr_reversed = []
    index = len(sorted_arr) - 1
    while index >= 0:
        sorted_arr_reversed.append(sorted_arr[index])
        index -= 1
    new_arr = []
    for var in sorted_arr_reversed:
        if var in dic:
            new_arr.append(dic[var])
    return new_arr