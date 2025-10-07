import collections

def remove_duplicates(numbers):
    count = collections.Counter(numbers)
    result = []
    for number in numbers:
        if count[number] <= 1:
            result.append(number)
    return result