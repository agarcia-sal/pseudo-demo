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
    for index in range(len(arr)):
        if 1 <= arr[index] <= 9:
            filtered_arr.append(arr[index])
    for i in range(len(filtered_arr) - 1):
        for j in range(len(filtered_arr) - 1 - i):
            if filtered_arr[j] > filtered_arr[j + 1]:
                temp = filtered_arr[j]
                filtered_arr[j] = filtered_arr[j + 1]
                filtered_arr[j + 1] = temp
    sorted_arr = []
    for k in range(len(filtered_arr) - 1, -1, -1):
        sorted_arr.append(filtered_arr[k])
    new_arr = []
    for m in range(len(sorted_arr)):
        num = sorted_arr[m]
        if num in dic:
            new_arr.append(dic[num])
    return new_arr