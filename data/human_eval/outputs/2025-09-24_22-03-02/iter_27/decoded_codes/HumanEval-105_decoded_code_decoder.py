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
    filtered_arr = []
    arr_length = len(arr)
    index = 0
    while index < arr_length:
        if 1 <= arr[index] <= 9:
            filtered_arr.append(arr[index])
        index += 1
    sorted_arr = []
    filtered_length = len(filtered_arr)
    for i in range(filtered_length):
        min_index = i
        for j in range(i + 1, filtered_length):
            if filtered_arr[j] < filtered_arr[min_index]:
                min_index = j
        temp = filtered_arr[i]
        filtered_arr[i] = filtered_arr[min_index]
        filtered_arr[min_index] = temp
    for k in range(filtered_length - 1, -1, -1):
        sorted_arr.append(filtered_arr[k])
    new_arr = []
    sorted_length = len(sorted_arr)
    m = 0
    while m < sorted_length:
        val = sorted_arr[m]
        name = dic[val]
        new_arr.append(name)
        m += 1
    return new_arr