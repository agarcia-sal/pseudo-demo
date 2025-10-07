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
        9: "Nine",
    }
    filtered_arr = []
    for i in range(len(arr)):
        if 1 <= arr[i] <= 9:
            filtered_arr.append(arr[i])
    n = len(filtered_arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if filtered_arr[j] > filtered_arr[j + 1]:
                temp = filtered_arr[j]
                filtered_arr[j] = filtered_arr[j + 1]
                filtered_arr[j + 1] = temp
    reversed_arr = []
    for k in range(len(filtered_arr) - 1, -1, -1):
        reversed_arr.append(filtered_arr[k])
    new_arr = []
    for m in range(len(reversed_arr)):
        current_value = reversed_arr[m]
        current_name = dic[current_value]
        new_arr.append(current_name)
    return new_arr