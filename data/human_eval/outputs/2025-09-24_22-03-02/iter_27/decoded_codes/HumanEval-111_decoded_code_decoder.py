def histogram(test):
    dict1 = {}
    list1 = test.split(" ")
    t = 0

    for index_i in range(len(list1)):
        i = list1[index_i]
        if list1.count(i) > t and i != "":
            t = list1.count(i)

    if t > 0:
        for index_i in range(len(list1)):
            i = list1[index_i]
            if list1.count(i) == t:
                dict1[i] = t

    return dict1