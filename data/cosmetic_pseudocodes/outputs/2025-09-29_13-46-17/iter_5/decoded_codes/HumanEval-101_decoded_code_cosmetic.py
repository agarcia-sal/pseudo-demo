from typing import List


def words_string(input_string: str) -> List[str]:
    def helper_chars(accumulator: List[str], index: int) -> List[str]:
        if index >= len(input_string):
            return accumulator

        current_char = input_string[index]
        updated_acc = accumulator + [' '] if current_char == ',' else accumulator + [current_char]

        return helper_chars(updated_acc, index + 1)

    if input_string != "":
        collected_list = helper_chars([], 0)
        combined = "".join(collected_list)

        splitted: List[str] = []
        word = ""

        for c in combined:
            if c == ' ':
                if word != "":
                    splitted.append(word)
                    word = ""
            else:
                word += c

        if word != "":
            splitted.append(word)

        return splitted
    else:
        return []