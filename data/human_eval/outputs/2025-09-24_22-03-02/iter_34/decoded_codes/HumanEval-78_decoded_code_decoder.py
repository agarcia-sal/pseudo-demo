def hex_key(num) -> int:
    primes = ['2', '3', '5', '7', 'B', 'D']
    total = 0
    length = len(num)
    for i in range(length):
        current_char = num[i]
        found = False
        for j in range(len(primes)):
            if current_char == primes[j]:
                found = True
                break
        if found:
            total += 1
    return total