def sort_array(arr):
    sorted_by_value = []
    length_arr = len(arr)
    for index_value in range(length_arr):
        sorted_by_value.append(arr[index_value])
    sorted_by_value.sort()

    sorted_by_ones = []
    length_sorted_by_value = len(sorted_by_value)
    for index_value in range(length_sorted_by_value):
        current_value = sorted_by_value[index_value]
        binary_string = ""
        temp_value = current_value
        if temp_value == 0:
            binary_string = "0"
        elif temp_value > 0:
            while temp_value > 0:
                remainder = temp_value % 2
                temp_value //= 2
                binary_string = str(remainder) + binary_string
        else:
            positive_temp = abs(temp_value)
            binary_string = ""
            while positive_temp > 0:
                remainder = positive_temp % 2
                positive_temp //= 2
                binary_string = str(remainder) + binary_string

        count_ones = 0
        length_binary = len(binary_string)
        for index_char in range(length_binary):
            if binary_string[index_char] == "1":
                count_ones += 1

        sorted_by_ones.append([current_value, count_ones])

    length_sorted_by_ones = len(sorted_by_ones)
    for i in range(length_sorted_by_ones - 1):
        for j in range(length_sorted_by_ones - 1 - i):
            if sorted_by_ones[j][1] > sorted_by_ones[j + 1][1]:
                temp = sorted_by_ones[j]
                sorted_by_ones[j] = sorted_by_ones[j + 1]
                sorted_by_ones[j + 1] = temp

    for i in range(length_sorted_by_ones - 1):
        for j in range(length_sorted_by_ones - 1 - i):
            if sorted_by_ones[j][1] == sorted_by_ones[j + 1][1]:
                if sorted_by_ones[j][0] > sorted_by_ones[j + 1][0]:
                    temp = sorted_by_ones[j]
                    sorted_by_ones[j] = sorted_by_ones[j + 1]
                    sorted_by_ones[j + 1] = temp

    result = []
    for index_value in range(length_sorted_by_ones):
        result.append(sorted_by_ones[index_value][0])
    return result