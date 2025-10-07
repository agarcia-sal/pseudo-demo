from typing import List


def count_nums(array_of_integers: List[int]) -> int:
    def digits_sum(integer_value: int) -> int:
        factor_sign = 1

        # Convert negative number to positive and adjust factor_sign accordingly
        while True:
            if integer_value < 0:
                integer_value = integer_value * (-1)
                factor_sign = -1
                break
            else:
                break

        digit_chars: List[str] = []
        int_as_string = ""
        idx_counter = 0
        s = str(integer_value)

        # Extract digits as characters
        while idx_counter < len(s):
            ch = s[idx_counter]
            digit_chars.append(ch)
            idx_counter += 1

        list_of_digits: List[int] = []
        iter_idx = 0

        # Convert each character digit to int using explicit if-else mapping
        while iter_idx < len(digit_chars):
            single_digit_str = digit_chars[iter_idx]
            single_digit_int = 0
            pow_idx = 0
            max_pow = len(single_digit_str)

            while pow_idx < max_pow:
                val_to_add = 0
                c = single_digit_str[pow_idx]
                if c == '0':
                    val_to_add = 0
                elif c == '1':
                    val_to_add = 1
                elif c == '2':
                    val_to_add = 2
                elif c == '3':
                    val_to_add = 3
                elif c == '4':
                    val_to_add = 4
                elif c == '5':
                    val_to_add = 5
                elif c == '6':
                    val_to_add = 6
                elif c == '7':
                    val_to_add = 7
                elif c == '8':
                    val_to_add = 8
                elif c == '9':
                    val_to_add = 9

                single_digit_int += val_to_add
                pow_idx += 1

            list_of_digits.append(single_digit_int)
            iter_idx += 1

        first_idx_digit = list_of_digits[0]
        list_of_digits[0] = first_idx_digit * factor_sign

        running_sum = 0
        sum_idx = 0
        while sum_idx < len(list_of_digits):
            running_sum += list_of_digits[sum_idx]
            sum_idx += 1

        return running_sum

    temp_storage: List[int] = []
    pos_counter = 0

    while pos_counter < len(array_of_integers):
        element_val = array_of_integers[pos_counter]
        computed_sum = digits_sum(element_val)
        temp_storage.append(computed_sum)
        pos_counter += 1

    positive_filtered: List[int] = []
    filt_idx = 0

    while filt_idx < len(temp_storage):
        val_check = temp_storage[filt_idx]
        if val_check > 0:
            positive_filtered.append(val_check)
        filt_idx += 1

    return len(positive_filtered)