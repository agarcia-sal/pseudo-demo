def fruit_distribution(s, n):
    list_of_numbers = []
    for word in s.split():
        if word.isdigit():
            list_of_numbers.append(int(word))
    return n - sum(list_of_numbers)