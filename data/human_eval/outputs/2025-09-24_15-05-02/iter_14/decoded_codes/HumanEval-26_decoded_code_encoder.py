def remove_duplicates(list_of_numbers):
    import collections
    counts = collections.Counter(list_of_numbers)
    result = []
    for number in list_of_numbers:
        if counts[number] <= 1:
            result.append(number)
    return result