def search(lst):
    if not lst:
        return -1  # Handle empty list edge case

    max_value = max(lst)
    frequency_list = [0] * (max_value + 1)

    for i in lst:
        frequency_list[i] += 1

    answer = -1
    for i in range(1, len(frequency_list)):
        if frequency_list[i] >= i:
            answer = i

    return answer