def get_odd_collatz(n: int) -> list[int]:
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
    for current_value in odd_collatz:
        inserted = False
        position = 0
        while position < len(sorted_list) and not inserted:
            if current_value < sorted_list[position]:
                sorted_list.insert(position, current_value)
                inserted = True
            position += 1
        if not inserted:
            sorted_list.append(current_value)

    return sorted_list