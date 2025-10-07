def skjkasdkd(lst) -> int:
    def isPrime(n: int) -> bool:
        limit = int(n ** 0.5) + 1
        i = 2
        while i < limit:
            if n % i == 0:
                return False
            i += 1
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        current_element = lst[i]
        is_prime_result = isPrime(current_element)
        if current_element > maxx and is_prime_result:
            maxx = current_element
        i += 1

    maxx_str = str(maxx)
    total = 0
    j = 0
    while j < len(maxx_str):
        char = maxx_str[j]
        digit = int(char)
        total += digit
        j += 1

    return total