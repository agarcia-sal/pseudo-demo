class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        total_sets = 0
        unique_elements = set()

        def max_partitions(s_: str, k_: int) -> int:
            nonlocal total_sets, unique_elements

            total_sets = 0
            unique_elements = set()

            def process_chars(position: int) -> int:
                nonlocal total_sets, unique_elements
                if position >= len(s_):
                    final_count = total_sets
                    if len(unique_elements) != 0:
                        final_count += 1
                    return final_count

                current_char = s_[position]
                if len(unique_elements) < k_:
                    unique_elements.add(current_char)
                    return process_chars(position + 1)
                else:
                    if current_char in unique_elements:
                        return process_chars(position + 1)
                    else:
                        total_sets += 1
                        unique_elements = {current_char}
                        return process_chars(position + 1)

            max_pieces = process_chars(0)

            def letters_generator(char_code: int):
                if char_code > 122:  # 'z'
                    return
                yield chr(char_code)
                yield from letters_generator(char_code + 1)

            def iterate_i(i_var: int):
                nonlocal max_pieces
                if i_var >= len(s_) - 1:
                    return

                def iterate_letters(chars_iter):
                    nonlocal max_pieces
                    if not chars_iter:
                        return
                    current_char = chars_iter[0]
                    remaining_chars = chars_iter[1:]
                    if current_char == s_[i_var]:
                        iterate_letters(remaining_chars)
                        return
                    prefix_substring = s_[:i_var]
                    suffix_substring = s_[i_var+1:]
                    candidate_string = prefix_substring + current_char + suffix_substring
                    candidate_val = max_partitions(candidate_string, k_)
                    if candidate_val > max_pieces:
                        max_pieces = candidate_val
                    iterate_letters(remaining_chars)

                iterate_letters(list(letters_generator(97)))  # generate letters from 'a' to 'z'
                iterate_i(i_var + 1)

            iterate_i(0)
            return max_pieces

        return max_partitions(s, k)