def match_parens(lst):
    def check(string):
        balance = 0
        for char in string:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    concatenation1 = lst[0] + lst[1]
    concatenation2 = lst[1] + lst[0]

    if check(concatenation1) or check(concatenation2):
        return 'Yes'
    else:
        return 'No'