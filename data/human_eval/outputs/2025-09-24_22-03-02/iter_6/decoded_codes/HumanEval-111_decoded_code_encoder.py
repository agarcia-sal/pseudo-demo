def histogram(test) -> dict:
    dict1 = {}
    list1 = test.split()
    max_count = 0

    for letter in list1:
        if letter and list1.count(letter) > max_count:
            max_count = list1.count(letter)

    if max_count > 0:
        for letter in list1:
            if list1.count(letter) == max_count:
                dict1[letter] = max_count

    return dict1