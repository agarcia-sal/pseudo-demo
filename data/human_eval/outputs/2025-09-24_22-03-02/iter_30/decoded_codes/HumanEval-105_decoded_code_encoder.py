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
    filtered_arr = [element for element in arr if 1 <= element <= 9]
    sorted_arr = []
    while filtered_arr:
        max_index = 0
        max_value = filtered_arr[0]
        for idx in range(1, len(filtered_arr)):
            if filtered_arr[idx] > max_value:
                max_value = filtered_arr[idx]
                max_index = idx
        sorted_arr.append(max_value)
        filtered_arr.pop(max_index)
    new_arr = [dic[var] for var in sorted_arr]
    return new_arr