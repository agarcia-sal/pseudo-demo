def hex_key(num: str) -> int:
    primes = ['2', '3', '5', '7', 'B', 'D']
    total = 0
    length_of_num = len(num)
    for i in range(length_of_num):
        current_character = num[i]
        if current_character in primes:
            total += 1
    return total