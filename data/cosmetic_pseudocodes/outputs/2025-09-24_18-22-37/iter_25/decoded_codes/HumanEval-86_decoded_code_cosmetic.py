from typing import List


def anti_shuffle(qwerty: str) -> str:
    zxcvb: List[str] = []
    poiuy: int = 0
    words = qwerty.split(" ")
    while poiuy < len(words):
        mnbvc = words[poiuy]
        lkjas: List[str] = []
        edcrf: int = 0
        while edcrf < len(mnbvc):
            lkjas.append(mnbvc[edcrf])
            edcrf += 1
        lkjas.sort()
        hjklq: str = ""
        edcrf = 0
        while edcrf < len(lkjas):
            hjklq += lkjas[edcrf]
            edcrf += 1
        zxcvb.append(hjklq)
        poiuy += 1
    result_string = ""
    xcvbn = 0
    while xcvbn < (len(zxcvb) - 1):
        result_string += zxcvb[xcvbn] + " "
        xcvbn += 1
    if len(zxcvb) > 0:
        result_string += zxcvb[len(zxcvb) - 1]
    return result_string