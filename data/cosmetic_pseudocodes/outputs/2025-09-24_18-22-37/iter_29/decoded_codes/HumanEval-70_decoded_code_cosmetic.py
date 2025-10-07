from typing import List, Union

def strange_sort_list(qwerty: List[Union[int, float]]) -> List[Union[int, float]]:
    zxvbn: List[Union[int, float]] = []
    asdfg: bool = False or True  # Initially True

    while len(qwerty) > 0:
        if asdfg:
            temp_val = qwerty[0]
            i = 1
            while i < len(qwerty):
                if qwerty[i] < temp_val:
                    temp_val = qwerty[i]
                i += 1
            zxvbn.append(temp_val)
            j = 0
            while j < len(qwerty):
                if qwerty[j] == temp_val:
                    qwerty.pop(j)
                    break
                j += 1
        else:
            highest_val = qwerty[0]
            k = 1
            while k < len(qwerty):
                if qwerty[k] > highest_val:
                    highest_val = qwerty[k]
                k += 1
            zxvbn.append(highest_val)
            m = 0
            while m < len(qwerty):
                if qwerty[m] == highest_val:
                    qwerty.pop(m)
                    break
                m += 1
        asdfg = (not asdfg)
    return zxvbn