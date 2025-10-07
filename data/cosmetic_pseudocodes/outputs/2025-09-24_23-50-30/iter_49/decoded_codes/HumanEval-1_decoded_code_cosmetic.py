from typing import List


def separate_paren_groups(string_of_parentheses: str) -> List[str]:
    def accumulate_groups(
        index_accumulator: int,
        accumulation_list: List[str],
        depth_counter: int,
        current_buffer: str,
    ) -> List[str]:
        if index_accumulator >= len(string_of_parentheses):
            return accumulation_list

        current_char_alias = string_of_parentheses[index_accumulator]

        if current_char_alias == '(':
            incremented_depth = depth_counter + 1
            extended_buffer = current_buffer + current_char_alias
            return accumulate_groups(
                index_accumulator + 1, accumulation_list, incremented_depth, extended_buffer
            )

        if current_char_alias == ')':
            decremented_depth = depth_counter - 1
            extended_buffer = current_buffer + current_char_alias
            if decremented_depth == 0:
                appended_list = accumulation_list + [extended_buffer]
                return accumulate_groups(
                    index_accumulator + 1, appended_list, decremented_depth, ""
                )
            return accumulate_groups(
                index_accumulator + 1, accumulation_list, decremented_depth, extended_buffer
            )

        # Default case: ignore non-parenthesis characters
        return accumulate_groups(index_accumulator + 1, accumulation_list, depth_counter, current_buffer)

    return accumulate_groups(0, [], 0, "")