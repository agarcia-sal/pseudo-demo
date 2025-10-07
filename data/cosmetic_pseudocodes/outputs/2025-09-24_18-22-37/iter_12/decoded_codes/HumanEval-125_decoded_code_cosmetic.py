from typing import Union, List

def split_words(arg1: str) -> Union[List[str], int]:
    if " " in arg1:
        arg3: List[str] = arg1.split(" ")
        return arg3
    else:
        if "," in arg1:
            arg2: str = arg1.replace(",", " ")
            return arg2.split(" ")
        else:
            arg4: int = 0
            for arg5 in range(len(arg1)):
                arg6: str = arg1[arg5]
                if "a" <= arg6 <= "z":
                    if (ord(arg6) % 2) == 0:
                        arg4 += 1
            return arg4