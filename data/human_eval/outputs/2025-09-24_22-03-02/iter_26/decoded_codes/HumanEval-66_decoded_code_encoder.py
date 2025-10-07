def digitSum(s):
    if s == '':
        return 0
    total_sum = 0
    for index in range(len(s)):
        char = s[index]
        if char.isupper():
            char_value = ord(char)
        else:
            char_value = 0
        total_sum += char_value
    return total_sum