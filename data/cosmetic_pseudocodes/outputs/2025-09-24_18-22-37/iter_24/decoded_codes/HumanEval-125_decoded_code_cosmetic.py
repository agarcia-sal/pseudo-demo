from typing import List, Union


def split_words(arg1: str) -> Union[List[str], int]:
    temp_flag1: bool = False
    temp_flag2: bool = False
    temp_string1: str = ""
    temp_count: int = 0
    temp_list1: List[str] = []

    # Check if there's a space in arg1
    i: int = 0
    while i < len(arg1):
        if arg1[i] == ' ':
            temp_flag1 = True
            break
        i += 1

    if temp_flag1:
        temp_list1 = []
        idx: int = 0
        while idx < len(arg1):
            ch = arg1[idx]
            if ch != ' ':
                temp_string1 += ch
            else:
                if temp_string1 != "":
                    temp_list1.append(temp_string1)
                    temp_string1 = ""
            idx += 1
        if temp_string1 != "":
            temp_list1.append(temp_string1)
            temp_string1 = ""
        return temp_list1
    else:
        # Check if there's a comma in arg1
        j: int = 0
        while j < len(arg1):
            if arg1[j] == ',':
                temp_flag2 = True
                break
            j += 1

        if temp_flag2:
            temp_string1 = ""
            k: int = 0
            while k < len(arg1):
                if arg1[k] == ',':
                    temp_string1 += ' '
                else:
                    temp_string1 += arg1[k]
                k += 1

            temp_list1 = []
            a: int = 0
            temp_word: str = ""
            while a < len(temp_string1):
                ch2 = temp_string1[a]
                if ch2 != ' ':
                    temp_word += ch2
                else:
                    if temp_word != "":
                        temp_list1.append(temp_word)
                        temp_word = ""
                a += 1
            if temp_word != "":
                temp_list1.append(temp_word)
                temp_word = ""
            return temp_list1
        else:
            temp_count = 0
            b: int = 0
            while b < len(arg1):
                ch3 = arg1[b]
                temp_check1 = 'a' <= ch3 <= 'z'
                # ASCII code for ch3:
                ascii_ch3 = ord(ch3)
                temp_check2 = (ascii_ch3 % 2) == 0
                if temp_check1 and temp_check2:
                    temp_count += 1
                b += 1
            return temp_count