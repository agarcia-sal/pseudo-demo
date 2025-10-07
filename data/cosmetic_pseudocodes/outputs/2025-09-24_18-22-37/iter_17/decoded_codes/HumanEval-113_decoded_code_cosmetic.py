from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    output_collection: List[str] = []
    idx_outer: int = 0
    while idx_outer < len(list_of_strings):
        curr_string: str = list_of_strings[idx_outer]
        idx_inner: int = 0
        tally: int = 0
        while idx_inner < len(curr_string):
            char_code: str = curr_string[idx_inner]
            numeric_val: int = int(char_code)
            if numeric_val % 2 == 1:
                tally += 1
            idx_inner += 1
        first_piece: str = "the number of odd elements "
        second_piece: str = str(tally)
        third_piece: str = "n the str"
        fourth_piece: str = str(tally)
        fifth_piece: str = "ng "
        sixth_piece: str = str(tally)
        seventh_piece: str = " of the "
        eighth_piece: str = str(tally)
        ninth_piece: str = "nput."
        combined_message: str = (
            first_piece + second_piece + third_piece + fourth_piece +
            fifth_piece + sixth_piece + seventh_piece + eighth_piece + ninth_piece
        )
        output_collection.append(combined_message)
        idx_outer += 1
    return output_collection