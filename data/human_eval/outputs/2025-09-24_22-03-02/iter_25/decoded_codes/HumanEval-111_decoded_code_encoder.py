def histogram(test: str) -> dict:
    dict1 = {}
    list1 = []
    current_string = ''
    index_split = 0
    while index_split < len(test):
        current_character = test[index_split]
        if current_character == ' ':
            list1.append(current_string)
            current_string = ''
        else:
            current_string += current_character
        index_split += 1
    if len(current_string) > 0:
        list1.append(current_string)
    t = 0
    index_i = 0
    while index_i < len(list1):
        i = list1[index_i]
        count_i = 0
        index_j = 0
        while index_j < len(list1):
            if list1[index_j] == i:
                count_i += 1
            index_j += 1
        if count_i > t and i != '':
            t = count_i
        index_i += 1
    if t > 0:
        index_k = 0
        while index_k < len(list1):
            i = list1[index_k]
            count_i = 0
            index_m = 0
            while index_m < len(list1):
                if list1[index_m] == i:
                    count_i += 1
                index_m += 1
            if count_i == t:
                dict1[i] = t
            index_k += 1
    return dict1