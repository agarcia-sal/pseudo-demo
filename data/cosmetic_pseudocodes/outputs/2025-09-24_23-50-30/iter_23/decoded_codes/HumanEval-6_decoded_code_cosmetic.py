from typing import List

def parse_nested_parens(parens_str: str) -> List[int]:
    def parse_paren_group(segment: str) -> int:
        depth_ctr = 0
        peak_depth = 0
        for char in segment:
            if char == '(':
                depth_ctr += 1
                if depth_ctr > peak_depth:
                    peak_depth = depth_ctr
            else:
                depth_ctr -= 1
        return peak_depth

    sections = [s for s in parens_str.split(" ") if s != ""]
    return [parse_paren_group(s) for s in sections]