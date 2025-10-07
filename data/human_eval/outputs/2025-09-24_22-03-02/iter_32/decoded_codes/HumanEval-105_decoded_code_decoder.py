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
    for i in range(len(arr)):
        current_element = arr[i]
        if 1 <= current_element <= 9:
            filtered_arr.append(current_element)
    filtered_arr.sort()
    filtered_arr.reverse()
    new_arr = []
    for j in range(len(filtered_arr)):
        var = filtered_arr[j]
        value = dic[var]
        new_arr.append(value)
    return new_arr