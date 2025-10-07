from typing import List, Union


def split_words(input_string: str) -> Union[List[str], int]:
    def helper_split(buffer: str) -> List[str]:
        output_list: List[str] = []
        current_fragment: str = ""
        for ch in buffer:
            if ch == " ":
                if current_fragment != "":
                    output_list.append(current_fragment)
                    current_fragment = ""
            else:
                current_fragment += ch
        if current_fragment != "":
            output_list.append(current_fragment)
        return output_list

    if " " in input_string:
        return helper_split(input_string)
    elif "," in input_string:
        temp_buf = "".join(" " if sym == "," else sym for sym in input_string)
        return helper_split(temp_buf)
    else:
        idx: int = 0
        cnt: int = 0
        n: int = len(input_string)
        while idx < n:
            char_val = input_string[idx]
            if "a" <= char_val <= "z":
                ascii_val = ord(char_val)
                if ascii_val % 2 == 0:
                    cnt += 1
            idx += 1
        return cnt