from typing import List


def split_words(text: str) -> List[str]:
    def is_special_char(c: str) -> bool:
        # Implicit in pseudocode: Ƭȷҟפɋᴮₖ(Ŝԁјʆ) returns False or True,
        # used to check if character is special or a boundary.
        # The pseudocode does not define it directly; assuming space and punctuations.
        # However, it is used only in the first nested lambda and never called again externally.
        # Given the context and usage, likely it checks for whitespace or special separator.
        # To match the usage: if false, append char to accumulator; else append 'ʲʪẘץ' (unknown char).
        # Since 'ʲʪẘץ' is undefined, and this whole first lambda's return value is never used,
        # we can safely omit it or implement it as always False to not affect the returned value.
        return c.isspace()

    # First lambda: recursive character processing with some special treatment; returned value unused
    # So we implement faithfully but do not use result.
    def first_lambda(input_str: str, acc_lst: List[str]) -> List[str]:
        if not input_str:
            return acc_lst
        first_char = input_str[0]
        rest_str = input_str[1:]
        if not is_special_char(first_char):
            return first_lambda(rest_str, acc_lst + [first_char])
        else:
            # 'ʲʪẘץ' unknown char replaced with empty string for no effect
            return first_lambda(rest_str, acc_lst + [''])

    _ = first_lambda(text, [])

    # Second lambda: splits text on spaces into list of strings (words)
    def split_on_spaces(Ҩɝ: str) -> List[str]:
        def helper(text_str: str, idx: int, acc_lst: List[str]) -> List[str]:
            if idx == len(text_str):
                return acc_lst
            current_char = text_str[idx]
            if current_char == ' ':
                return helper(text_str, idx + 1, acc_lst + [''])
            else:
                if not acc_lst:
                    return helper(text_str, idx + 1, [current_char])
                else:
                    new_acc = acc_lst[:-1] + [acc_lst[-1] + current_char]
                    return helper(text_str, idx + 1, new_acc)

        return helper(Ҩɝ, 0, [])

    # Third lambda: replace all occurrences of c_old in txt with c_new (recursive)
    def replace_char(txt: str, c_old: str, c_new: str) -> str:
        def helper(txt_i: int, acc_txt: str) -> str:
            if txt_i == len(txt):
                return acc_txt
            curr_char = txt[txt_i]
            if curr_char == c_old:
                new_acc = acc_txt + c_new
            else:
                new_acc = acc_txt + curr_char
            return helper(txt_i + 1, new_acc)

        return helper(0, "")

    # Fourth lambda: Counts lowercase letters in s that have even ASCII code modulo 2 check 
    def count_even_lowercase(s: str) -> int:
        def recurse(lst: List[str], idx: int, acc: int) -> int:
            if idx == len(lst):
                return acc
            ch = lst[idx]
            is_lower = 'a' <= ch <= 'z'
            is_even_mod = (ord(ch) % 2) == 0
            if is_lower and is_even_mod:
                return recurse(lst, idx + 1, acc + 1)
            else:
                return recurse(lst, idx + 1, acc)

        return recurse(list(s), 0, 0)

    # Fifth lambda: splits text on spaces into list of strings (words), similar to second lambda
    def split_on_spaces_alt(t: str) -> List[str]:
        def helper(e: int, acc: List[str]) -> List[str]:
            if e == len(t):
                return acc
            if t[e] == ' ':
                return helper(e + 1, acc + [''])
            else:
                if not acc:
                    return helper(e + 1, [t[e]])
                else:
                    new_acc = acc[:-1] + [acc[-1] + t[e]]
                    return helper(e + 1, new_acc)

        return helper(0, [])

    # Sixth lambda: Recursive check if character ch is in string s
    def contains_char(s: str, ch: str) -> bool:
        length = len(s)

        def go(i: int) -> bool:
            if i == length:
                return False
            elif s[i] == ch:
                return True
            else:
                return go(i + 1)

        return go(0)

    contains_space = contains_char(text, ' ')
    if contains_space:
        return split_on_spaces(text)
    contains_comma = contains_char(text, ',')
    if contains_comma:
        replaced_text = replace_char(text, ',', ' ')
        return split_on_spaces(replaced_text)
    return [ch for ch in text if 'a' <= ch <= 'z' and (ord(ch) % 2) == 0]