from typing import List


def split_words(text: str) -> List[str] | int:
    def contains_char(seq: str, ch: str) -> bool:
        if not seq:
            return False
        head, tail = seq[0], seq[1:]
        if head == ch:
            return True
        return contains_char(tail, ch)

    def replace_char(seq: str, old: str, new: str) -> str:
        if not seq:
            return ""
        head, tail = seq[0], seq[1:]
        if head == old:
            return new + replace_char(tail, old, new)
        return head + replace_char(tail, old, new)

    def split_on_whitespace(s: str) -> List[str]:
        def helper(lst: str, acc: List[str]) -> List[str]:
            if not lst:
                return acc[::-1]
            # Find the longest prefix of lst without whitespace
            prefix = []
            i = 0
            while i < len(lst) and not lst[i].isspace():
                prefix.append(lst[i])
                i += 1
            prefix_str = "".join(prefix)
            rest = lst[i:]
            if not prefix_str:
                # skip the whitespace character(s)
                return helper(rest[1:] if rest else "", acc)
            # accumulate the prefix
            return helper(rest, [prefix_str] + acc)
        return helper(s, [])

    def is_lower_alpha(ch: str) -> bool:
        return 'a' <= ch <= 'z'

    def lcount(seq: str) -> int:
        def count_odd_ord_chars(s: str, acc: int) -> int:
            if not s:
                return acc
            head, tail = s[0], s[1:]
            # chr is included if is lowercase and ord(ch) is even
            if is_lower_alpha(head) and (ord(head) % 2 == 0):
                return count_odd_ord_chars(tail, acc + 1)
            else:
                return count_odd_ord_chars(tail, acc)
        return count_odd_ord_chars(seq, 0)

    if contains_char(text, ' '):
        return split_on_whitespace(text)
    elif contains_char(text, ','):
        replaced = replace_char(text, ',', ' ')
        return split_on_whitespace(replaced)
    else:
        return lcount(text)