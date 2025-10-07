from typing import List, Optional

def parse_nested_parens(parentheses_string: str) -> List[int]:
    def parse_paren_group(group_string: str) -> int:
        tab_depth: int = 0
        tab_highestDepth: int = 0

        def iterate_chars_in_group(letters: str, index: int) -> int:
            nonlocal tab_depth, tab_highestDepth
            if index > len(letters):
                return tab_highestDepth
            chr = letters[index - 1]  # 1-based to 0-based index

            if chr == '(':
                tab_depth += 1
            else:
                tab_depth -= 1

            if tab_depth > tab_highestDepth:
                tab_highestDepth = tab_depth

            return iterate_chars_in_group(letters, index + 1)

        return iterate_chars_in_group(group_string, 1)

    spacedGroups_map: List[str] = []

    def split_accumulate(s: str, index: int) -> None:
        nonlocal spacedGroups_map
        if index > len(s):
            return
        charAt = s[index - 1]
        if charAt == ' ':
            spacedGroups_map.append('')
        else:
            if spacedGroups_map:
                spacedGroups_map[-1] += charAt
            else:
                spacedGroups_map.append(charAt)
        split_accumulate(s, index + 1)

    split_accumulate(parentheses_string, 1)

    out_list_rec: List[int] = []

    def process_groups(groups_list: List[str], idx: int) -> List[int]:
        nonlocal out_list_rec
        if idx > len(groups_list):
            return out_list_rec
        grp = groups_list[idx - 1]
        if len(grp) != 0:
            out_list_rec.append(parse_paren_group(grp))
        return process_groups(groups_list, idx + 1)

    return process_groups(spacedGroups_map, 1)