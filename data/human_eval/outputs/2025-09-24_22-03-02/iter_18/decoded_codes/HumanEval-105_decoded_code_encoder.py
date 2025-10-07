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
    # selection sort ascending
    for i in range(len(filtered_arr)):
        current_min = filtered_arr[i]
        current_index = i
        for j in range(i, len(filtered_arr)):
            if filtered_arr[j] < current_min:
                current_min = filtered_arr[j]
                current_index = j
        filtered_arr[i], filtered_arr[current_index] = filtered_arr[current_index], filtered_arr[i]
    sorted_arr = []
    for i in range(len(filtered_arr) - 1, -1, -1):
        sorted_arr.append(filtered_arr[i])
    new_arr = [dic[var] for var in sorted_arr if var in dic]
    return new_arr