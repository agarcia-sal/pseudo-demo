from typing import List, Union


def split_words(arg1: str) -> Union[int, List[str]]:
    if ' ' not in arg1:
        if ',' not in arg1:
            acc1: int = 0
            v1: List[str] = list(arg1)
            i1: int = 0
            while True:
                if i1 >= len(v1):
                    break
                ch1: str = v1[i1]
                if ch1.islower():
                    code1: int = ord(ch1)
                    if code1 % 2 == 0:
                        acc1 += 1
                i1 += 1
            return acc1
        else:
            tmp1: str = ''
            j1: int = 0
            src1: List[str] = list(arg1)
            while j1 < len(src1):
                if src1[j1] == ',':
                    tmp1 += ' '
                else:
                    tmp1 += src1[j1]
                j1 += 1
            res1: List[str] = tmp1.split()
            return res1
    else:
        return arg1.split()