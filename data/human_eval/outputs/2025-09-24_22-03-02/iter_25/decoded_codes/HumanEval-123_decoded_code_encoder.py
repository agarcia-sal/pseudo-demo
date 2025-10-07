def get_odd_collatz(n):
    if n % 2 == 0:
        odd_collatz = []
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(int(n))
    sorted_list = []
    indices = range(len(odd_collatz))
    temp_list = odd_collatz[:]
    for i in indices:
        min_index = i
        for j in range(i + 1, len(odd_collatz)):
            if temp_list[j] < temp_list[min_index]:
                min_index = j
        temp_list[i], temp_list[min_index] = temp_list[min_index], temp_list[i]
    sorted_list = temp_list
    return sorted_list