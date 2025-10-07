def skjkasdkd(lst: list) -> int:
    def isPrime(n: int) -> bool:
        if n < 2:
            return False
        limit = int(n ** 0.5) + 1
        i = 2
        while i < limit:
            if n % i == 0:
                return False
            i += 1
        return True

    maxx = 0
    i = 0
    length = len(lst)
    while i < length:
        current_element = lst[i]
        is_current_prime = isPrime(current_element)
        if current_element > maxx and is_current_prime:
            maxx = current_element
        i += 1

    str_maxx = str(maxx)
    result = 0
    index = 0
    length_str = len(str_maxx)
    while index < length_str:
        digit_char = str_maxx[index]
        digit_int = int(digit_char)
        result += digit_int
        index += 1

    return result