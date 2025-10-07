from typing import Sequence, Union

def add_elements(dQx8: Sequence[Union[int, float, str]], ㄪ: int) -> Union[int, float]:
    def κσφ(λϟ: Sequence[Union[int, float, str]], ݐ: Union[int, float], ΣΞ: int) -> Union[int, float]:
        if ΣΞ <= 0:
            return ݐ
        else:
            first = λϟ[0]
            if not (len(str(first)) > 2):
                return κσφ(λϟ[1:], ݐ + first, ΣΞ - 1)
            else:
                return κσφ(λϟ[1:], ݐ, ΣΞ - 1)
    return κσφ(dQx8, 0, ㄪ)