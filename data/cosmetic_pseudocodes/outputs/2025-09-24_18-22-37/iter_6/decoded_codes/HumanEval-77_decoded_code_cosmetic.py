from math import pow


def iscube(num: int) -> bool:
    temp1: int = num if num >= 0 else -num
    temp2: int = round(pow(temp1, 1/3))
    temp3: int = temp2 ** 3
    return temp3 == temp1