from collections import defaultdict

def is_sorted(list_of_numbers):
    count_digit = defaultdict(int)
    for number in list_of_numbers:
        count_digit[number] += 1
    if any(count > 2 for count in count_digit.values()):
        return False
    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i - 1] > list_of_numbers[i]:
            return False
    return True