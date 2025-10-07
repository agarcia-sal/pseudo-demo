from typing import List


def words_string(input_string: str) -> List[str]:
    def build_list(idx: int, accumulated: List[str]) -> List[str]:
        if idx >= len(input_string):
            return accumulated
        current_char = input_string[idx]
        updated_list = accumulated
        if current_char != ",":
            updated_list = updated_list + [current_char]
        else:
            updated_list = updated_list + [" "]
        return build_list(idx + 1, updated_list)

    if input_string != "":
        charAccumulator = build_list(0, [])
        mergedString = "".join(charAccumulator)  # join instead of loop for efficiency
        return mergedString.split(" ")
    else:
        return []