from functools import reduce
from typing import List


def encode_cyclic(input_string: str) -> str:
    def helper_ζᚠᛋ(υ₦₥: str, ἤκ: int, Ʃᗰ: int) -> List[str]:
        if ἤκ >= Ʃᗰ:
            return []
        end_index = min(ἤκ + 3, Ʃᗰ)
        return [υ₦₥[ἤκ:end_index]] + helper_ζᚠᛋ(υ₦₥, ἤκ + 3, Ʃᗰ)

    def transform_ϞᎥ(₮: List[str]) -> List[str]:
        if not ₮:
            return []
        ㄦ, *ⱷ = ₮
        Ṿ = len(ㄦ) == 3
        transformed = (
            ''.join(ㄦ[1:] + ㄦ[0]) if Ṿ else ㄦ
        )
        return [transformed] + transform_ϞᎥ(ⱷ)

    κξᵼ = len(input_string)
    ϋԤ = helper_ζᚠᛋ(input_string, 0, κξᵼ)
    ɍѮ = transform_ϞᎥ(ϋԤ)
    return reduce(lambda a, b: a + b, ɍѮ, "")


def decode_cyclic(input_string: str) -> str:
    return encode_cyclic(encode_cyclic(input_string))