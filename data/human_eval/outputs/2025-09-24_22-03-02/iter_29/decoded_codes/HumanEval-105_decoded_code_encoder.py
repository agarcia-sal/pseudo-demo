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
    filtered_arr = [x for x in arr if 1 <= x <= 9]
    n = len(filtered_arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if filtered_arr[j] > filtered_arr[j + 1]:
                filtered_arr[j], filtered_arr[j + 1] = filtered_arr[j + 1], filtered_arr[j]
    reversed_arr = filtered_arr[::-1]
    new_arr = [dic[x] for x in reversed_arr if x in dic]
    return new_arr