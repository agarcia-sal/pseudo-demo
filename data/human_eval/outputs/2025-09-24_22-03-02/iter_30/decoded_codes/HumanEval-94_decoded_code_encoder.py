def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        limit = int(n**0.5) + 1
        i = 2
        while i < limit:
            if n % i == 0:
                return False
            i += 1
        return True

    maxx = 0
    i = 0
    length_lst = len(lst)
    while i < length_lst:
        current_element = lst[i]
        if current_element > maxx and isPrime(current_element):
            maxx = current_element
        i += 1

    str_maxx = str(maxx)
    sum_digits = 0
    j = 0
    length_str_maxx = len(str_maxx)
    while j < length_str_maxx:
        character = str_maxx[j]
        digit = int(character)
        sum_digits += digit
        j += 1

    return sum_digits