def histogram(test) -> dict:
    dict1 = {}
    list1 = test.split(" ")
    t = 0

    for i in list1:
        count_i = 0
        for element in list1:
            if element == i:
                count_i += 1
        if count_i > t and i != "":
            t = count_i

    if t > 0:
        for i in list1:
            count_i = 0
            for element in list1:
                if element == i:
                    count_i += 1
            if count_i == t:
                dict1[i] = t

    return dict1