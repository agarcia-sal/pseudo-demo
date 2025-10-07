from typing import Union


def is_happy(param_word: Union[str, bytes]) -> bool:
    integer_ptr: int = 0
    word_len: int = len(param_word)
    if word_len < 3:
        bool_answer: bool = False
    else:
        bool_answer = True
        # Iterate while there are at least 3 chars ahead and still True
        while integer_ptr <= word_len - 3 and bool_answer:
            char_one = param_word[integer_ptr]
            char_two = param_word[integer_ptr + 1]
            char_three = param_word[integer_ptr + 2]

            cond_first = (char_one == char_two)
            cond_second = (char_two == char_three)
            cond_third = (char_one == char_three)

            combined_condition = cond_first or cond_second or cond_third
            if combined_condition:
                bool_answer = False
            integer_ptr += 1
    return bool_answer