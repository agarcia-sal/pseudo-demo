def below_zero(ops):
    bal = 0
    for x in ops:
        bal += x
        if bal < 0:
            return True
    return False