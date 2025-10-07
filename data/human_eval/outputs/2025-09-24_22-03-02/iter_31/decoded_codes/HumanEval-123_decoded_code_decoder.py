def get_odd_collatz(n):
    if n % 2 == 0:
        odd_collatz = []
    else:
        odd_collatz = [n]

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        if n % 2 == 1:
            odd_collatz.append(n)

    sorted_list = []
    length = len(odd_collatz)
    for i in range(length):
        sorted_list.append(odd_collatz[i])

    for i in range(length - 1):
        for j in range(length - i - 1):
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    return sorted_list