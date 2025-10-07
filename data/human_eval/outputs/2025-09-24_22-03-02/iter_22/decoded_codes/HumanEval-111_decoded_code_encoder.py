def histogram(test: str) -> dict:
    dict1 = {}
    list1 = test.split(" ")
    t = 0

    for i in range(len(list1)):
        current_element = list1[i]
        count = 0
        for j in range(len(list1)):
            if list1[j] == current_element:
                count += 1
        if count > t and current_element != '':
            t = count

    if t > 0:
        for i in range(len(list1)):
            current_element = list1[i]
            count = 0
            for j in range(len(list1)):
                if list1[j] == current_element:
                    count += 1
            if count == t:
                dict1[current_element] = t

    return dict1