from typing import Union

def is_palindrome(vowel_alpha: str) -> bool:
    temp_a: str = vowel_alpha[::-1]
    result_flag: bool = (vowel_alpha == temp_a)
    return result_flag

def make_palindrome(mnemonic_delta: str) -> str:
    empty_check: bool = (mnemonic_delta == "")
    if not empty_check:
        index_tango: int = 0
        check_flag: bool = True
        while check_flag:
            slice_echo: str = mnemonic_delta[index_tango:]
            palindrome_status: bool = is_palindrome(slice_echo)
            if palindrome_status:
                check_flag = False
            else:
                index_tango += 1

        head_slice: str = mnemonic_delta[:index_tango]
        reversed_head: str = head_slice[::-1]
        concatenated_str: str = mnemonic_delta + reversed_head
        return concatenated_str
    else:
        empty_str: str = ""
        return empty_str