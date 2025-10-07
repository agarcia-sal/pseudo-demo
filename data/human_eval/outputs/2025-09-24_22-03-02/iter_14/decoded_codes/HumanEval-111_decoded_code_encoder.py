def histogram(test):
    dict1 = {}
    list1 = test.split(" ")
    t = 0
    for i in list1:
        count_i = list1.count(i)
        if count_i > t and i != "":
            t = count_i
    if t > 0:
        for i in list1:
            if list1.count(i) == t:
                dict1[i] = t
    return dict1