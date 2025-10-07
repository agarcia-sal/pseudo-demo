def skjkasdkd(lst):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    maxx = 0
    i = 0
    while i < len(lst):
        if lst[i] > maxx and isPrime(lst[i]):
            maxx = lst[i]
        i += 1

    result = 0
    string_representation = str(maxx)
    index = 0
    while index < len(string_representation):
        character = string_representation[index]
        digit = int(character)
        result += digit
        index += 1

    return result