def solve(N):
    string_n = str(N)
    sum_digits = 0
    index = 0
    while index < len(string_n):
        char = string_n[index]
        digit = int(char)
        sum_digits += digit
        index += 1
    binary_string = ""
    if sum_digits == 0:
        binary_string = "0"
    else:
        temp = sum_digits
        binary_digits = [""]
        while temp > 0:
            remainder = temp % 2
            temp //= 2
            binary_digits.insert(0, str(remainder))
        index = 0
        while index < len(binary_digits):
            binary_string += binary_digits[index]
            index += 1
    return binary_string