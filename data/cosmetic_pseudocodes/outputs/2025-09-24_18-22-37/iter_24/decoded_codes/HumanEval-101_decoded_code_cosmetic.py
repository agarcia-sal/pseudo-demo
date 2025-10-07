from typing import List


def words_string(paragraph: str) -> List[str]:
    if paragraph:
        gathered_chars: List[str] = []
        pos_flag: int = 0
        while pos_flag < len(paragraph):
            current_symbol: str = paragraph[pos_flag]
            if current_symbol == ',':
                gathered_chars.append(' ')
            else:
                gathered_chars.append(current_symbol)
            pos_flag += 1

        result_string: str = ""
        ix: int = 0
        while ix < len(gathered_chars):
            result_string += gathered_chars[ix]
            ix += 1

        split_result: List[str] = []
        temp_word: str = ""
        idx: int = 0
        while idx < len(result_string):
            if result_string[idx] != ' ':
                temp_word += result_string[idx]
            else:
                if len(temp_word) > 0:
                    split_result.append(temp_word)
                    temp_word = ""
            idx += 1
        if len(temp_word) > 0:
            split_result.append(temp_word)

        return split_result
    else:
        return []