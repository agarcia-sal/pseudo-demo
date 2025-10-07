from typing import List

def words_string(input_string: str) -> List[str]:
    def process_chars(index: int, acc: List[str]) -> List[str]:
        if index >= len(input_string):
            return acc
        else:
            ch = input_string[index]
            if ch == ",":
                return process_chars(index + 1, acc + [" "])
            else:
                return process_chars(index + 1, acc + [ch])

    if input_string != "":
        transformed_list = process_chars(0, [])
        combined_str = "".join(transformed_list)
        return combined_str.split()
    else:
        return []