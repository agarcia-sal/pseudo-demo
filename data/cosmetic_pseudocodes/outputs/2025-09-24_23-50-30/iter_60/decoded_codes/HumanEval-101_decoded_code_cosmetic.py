from typing import List

def words_string(literal: str) -> List[str]:
    if literal == "":
        return []

    def NextChar(pos: int, acc: str) -> str:
        if pos >= len(literal):
            return acc
        acc2 = acc + (" " if literal[pos] == "," else literal[pos])
        return NextChar(pos + 1, acc2)

    final_str = NextChar(0, "")
    return final_str.split(" ")