def match_parens(list_of_two_strings):
    def check(string_s):
        val = 0
        for character in string_s:
            if character == '(':
                val += 1
            else:
                val -= 1
            if val < 0:
                return False
        return val == 0

    S1 = list_of_two_strings[0] + list_of_two_strings[1]
    S2 = list_of_two_strings[1] + list_of_two_strings[0]

    if check(S1) or check(S2):
        return 'Yes'
    else:
        return 'No'