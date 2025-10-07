from typing import List

def words_string(input_string: str) -> List[str]:
    if input_string != "":
        buffer: List[str] = []
        index: int = 0

        while index < len(input_string):
            symbol: str = input_string[index]
            if symbol != ",":
                buffer.append(symbol)
            else:
                buffer.append(" ")
            index += 1

        merged_text: str = ""
        for element in buffer:
            merged_text += element

        return merged_text.split(" ")
    else:
        return []