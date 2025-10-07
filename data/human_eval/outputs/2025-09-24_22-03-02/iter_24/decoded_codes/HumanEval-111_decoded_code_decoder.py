def histogram(test: str) -> dict:
    dict1 = {}
    list1 = test.split(" ")
    t = 0
    for index_i in range(len(list1)):
        i = list1[index_i]
        count_i = 0
        for index_x in range(len(list1)):
            if list1[index_x] == i:
                count_i += 1
        if count_i > t and i != "":
            t = count_i
    if t > 0:
        for index_j in range(len(list1)):
            i = list1[index_j]
            count_i = 0
            for index_y in range(len(list1)):
                if list1[index_y] == i:
                    count_i += 1
            if count_i == t:
                dict1[i] = t
    return dict1