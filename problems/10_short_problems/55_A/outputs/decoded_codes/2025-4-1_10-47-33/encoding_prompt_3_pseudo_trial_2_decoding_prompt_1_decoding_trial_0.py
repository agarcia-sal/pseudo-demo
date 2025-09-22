# START

# 1. DEFINE an integer variable `numberOfElements` and SET it to the input value
numberOfElements = int(input())

# 2. CREATE a list `isActive` initialized with `True` values of size `numberOfElements`
isActive = [True] * numberOfElements

# 3. INITIALIZE variables `index` to 0 and `step` to 1
index = 0
step = 1

# 4. WHILE `step` is less than or equal to 500000 DO
while step <= 500000:
    # a. IF `isActive[index]` is `True` THEN
    if isActive[index]:
        # i. SET `isActive[index]` to `False` (mark the index as inactive)
        isActive[index] = False
    
    # b. INCREMENT `step` by 1
    step += 1
    
    # c. UPDATE `index` to (current `index` + `step`) MOD `numberOfElements` (calculate the new active index)
    index = (index + step) % numberOfElements

# END WHILE

# 5. CREATE a list `activeElements` containing all elements in `isActive` that are still `True`
activeElements = [active for active in isActive if active]

# 6. IF the length of `activeElements` is 0 THEN
if len(activeElements) == 0:
    # a. PRINT 'YES' (indicating no active elements remaining)
    print('YES')
else:
    # a. PRINT 'NO' (indicating there are active elements remaining)
    print('NO')

# END
