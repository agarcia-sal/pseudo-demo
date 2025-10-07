def histogram(test):
    dict1 = {}
    list1 = test.split()
    t = 0

    for i in list1:
        cnt = list1.count(i)
        if cnt > t and i != '':
            t = cnt

    if t > 0:
        for i in list1:
            if list1.count(i) == t:
                dict1[i] = t

    return dict1