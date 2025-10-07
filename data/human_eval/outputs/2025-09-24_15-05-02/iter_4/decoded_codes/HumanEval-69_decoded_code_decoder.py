def search(lst):
    max_value = max(lst) if lst else 0
    frequency_list = [0] * (max_value + 1)

    for number in lst:
        frequency_list[number] += 1

    answer = -1
    for index in range(1, len(frequency_list)):
        if frequency_list[index] >= index:
            answer = index

    return answer