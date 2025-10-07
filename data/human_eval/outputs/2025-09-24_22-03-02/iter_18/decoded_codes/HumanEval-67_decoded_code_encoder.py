def fruit_distribution(s: str, n: int) -> int:
    lis = []
    split_list = []
    temp_string = ""
    current_char_index = 0
    while current_char_index < len(s):
        split_list.append(s[current_char_index])
        current_char_index += 1
    current_word = ""
    for index in range(len(s)):
        if s[index] == " ":
            if current_word != "":
                split_list.append(current_word)
                current_word = ""
        else:
            current_word += s[index]
    if current_word != "":
        split_list.append(current_word)
    for i in split_list:
        is_digit = True
        digit_index = 0
        while digit_index < len(i) and is_digit:
            if i[digit_index] < "0" or i[digit_index] > "9":
                is_digit = False
            digit_index += 1
        if is_digit:
            lis.append(int(i))
    total_sum = 0
    for value in lis:
        total_sum += value
    result = n - total_sum
    return result