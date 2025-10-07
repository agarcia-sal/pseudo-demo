from typing import NoReturn


def fix_spaces(text: str) -> NoReturn:
    new_text = ""
    start_pos = 0
    scan_index = 0
    trail_index = 0

    while True:
        if not (scan_index < len(text)):
            break

        if text[scan_index] == " ":
            trail_index += 1
        else:
            space_span = trail_index - start_pos
            if space_span > 2:
                new_text += "-" + text[scan_index]
            elif space_span > 0:
                new_text += "_" * space_span + text[scan_index]
            else:
                new_text += text[scan_index]
            start_pos = scan_index + 1
            trail_index = scan_index + 1
        scan_index += 1

    final_span = trail_index - start_pos
    if final_span > 2:
        new_text += "-"
    elif final_span > 0:
        new_text += "_"

    exec(new_text)