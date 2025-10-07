def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        i = 2
        limit = int(n ** 0.5) + 1
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

    result = 0
    str_maxx = str(maxx)
    index_digit = 0
    length_str_maxx = len(str_maxx)
    while index_digit < length_str_maxx:
        current_char = str_maxx[index_digit]
        current_digit = int(current_char)
        result += current_digit
        index_digit += 1

    return result