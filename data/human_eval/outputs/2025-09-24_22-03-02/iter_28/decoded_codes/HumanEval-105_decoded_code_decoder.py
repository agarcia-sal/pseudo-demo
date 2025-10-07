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
    length_arr = len(arr)
    for i in range(length_arr):
        element = arr[i]
        if 1 <= element <= 9:
            filtered_arr.append(element)
    length_filtered = len(filtered_arr)
    for j in range(length_filtered - 1):
        for k in range(length_filtered - 1 - j):
            if filtered_arr[k] > filtered_arr[k + 1]:
                temp = filtered_arr[k]
                filtered_arr[k] = filtered_arr[k + 1]
                filtered_arr[k + 1] = temp
    reversed_arr = []
    length_filtered = len(filtered_arr)
    for m in range(length_filtered - 1, -1, -1):
        reversed_arr.append(filtered_arr[m])
    new_arr = []
    length_reversed = len(reversed_arr)
    for n in range(length_reversed):
        number = reversed_arr[n]
        if number in dic:
            new_arr.append(dic[number])
    return new_arr