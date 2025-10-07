from typing import List

def anti_shuffle(input_string: str) -> str:
    def helper(remaining_words: List[str], accumulated_sorted: List[str]) -> List[str]:
        if not remaining_words:
            return accumulated_sorted
        current_word = remaining_words[0]
        chars_array = sorted(current_word)
        ordered_word = ''.join(chars_array)  # join sorted chars into a string
        return helper(remaining_words[1:], accumulated_sorted + [ordered_word])

    words_list = input_string.split(' ')
    sorted_words_list = helper(words_list, [])
    final_string = ' '.join(sorted_words_list)
    return final_string