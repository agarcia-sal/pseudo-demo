# 1. Start
# 2. Read an integer value `n` from input
n = int(input())

# 3. Create a list `isMarked` of size `n` and initialize all values to `True`
isMarked = [True] * n

# 4. Set variables `position` to 0 and `step` to 1
position = 0
step = 1

# 5. While `step` is less than or equal to 500,000, do the following:
while step <= 500000:
    # 1. If the value at the current `position` in `isMarked` is `True`:
    if isMarked[position]:
        # - Set the value at `position` in `isMarked` to `False`
        isMarked[position] = False
    
    # 2. Increment `step` by 1
    step += 1
    
    # 3. Update `position` to be the remainder when (`position` + `step`) is divided by `n`
    position = (position + step) % n

# 6. Create a list `unmarked` containing all `True` values from `isMarked`
unmarked = [value for value in isMarked if value]

# 7. If the length of `unmarked` is 0:
if len(unmarked) == 0:
    # - Output 'YES'
    print('YES')
# 8. Else:
else:
    # - Output 'NO'
    print('NO')
# 9. End
