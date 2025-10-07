def count_occurrences(list_input, element) -> int:
    count = 0
    for i in range(len(list_input)):
        if list_input[i] == element:
            count += 1
    return count

def histogram(test) -> dict:
    dict1 = {}
    list1 = []
    list1.extend(test.split(" "))
    t = 0

    for index in range(len(list1)):
        i = list1[index]
        cnt = count_occurrences(list1, i)
        if cnt > t and i != "":
            t = cnt

    if t > 0:
        for index in range(len(list1)):
            i = list1[index]
            if count_occurrences(list1, i) == t:
                dict1[i] = t

    return dict1