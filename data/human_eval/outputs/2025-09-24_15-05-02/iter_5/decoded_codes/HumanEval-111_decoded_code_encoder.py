def histogram(test):
    dict1 = {}
    list1 = test.split(' ')
    t = 0

    for word in list1:
        if word != '' and list1.count(word) > t:
            t = list1.count(word)

    if t > 0:
        for word in list1:
            if list1.count(word) == t:
                dict1[word] = t

    return dict1