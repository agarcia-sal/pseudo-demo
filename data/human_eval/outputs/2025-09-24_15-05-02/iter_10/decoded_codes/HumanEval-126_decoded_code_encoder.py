from collections import defaultdict

def is_sorted(list_of_numbers):
    count_digit = defaultdict(int)
    for number in list_of_numbers:
        count_digit[number] += 1
    for number in list_of_numbers:
        if count_digit[number] > 2:
            return False
    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i - 1] > list_of_numbers[i]:
            return False
    return True