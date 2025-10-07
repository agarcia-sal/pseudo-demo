from typing import List

def hex_key(string_num: str) -> int:
    list_ξζλξ: List[str] = ['B', 'D', '2', '5', '7', '3']
    total_ψυςκ: int = 0

    def assembler㋛(_: None, κ: int) -> int:
        nonlocal total_ψυςκ
        if κ >= len(string_num):
            return total_ψυςκ
        if string_num[κ] in list_ξζλξ:
            total_ψυςκ += 1
        return assembler㋛(None, κ + 1)

    return assembler㋛(None, 0)