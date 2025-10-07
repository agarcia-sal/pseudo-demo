from typing import List

def string_sequence(integer_q: int) -> str:
    resultList: List[str] = []
    iterator_r: int = 0
    while iterator_r <= integer_q:
        tempString_s: str = str(iterator_r)
        resultList.append(tempString_s)
        iterator_r += 1
    output_t: str = ""
    index_u: int = 0
    while index_u < len(resultList):
        if index_u == 0:
            output_t = resultList[index_u]
        else:
            output_t += " " + resultList[index_u]
        index_u += 1
    return output_t