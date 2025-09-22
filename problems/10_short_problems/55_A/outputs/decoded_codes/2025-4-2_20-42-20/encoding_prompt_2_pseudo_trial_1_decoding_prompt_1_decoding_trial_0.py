# 1. Start the program.
# (not explicitly needed in Python)

# 2. Get an integer input from the user and store it as `numberOfElements`.
numberOfElements = int(input())

# 3. Create a list `isAvailable` with `numberOfElements` elements, all initialized to `True`.
isAvailable = [True] * numberOfElements

# 4. Initialize a variable `index` to 0.
index = 0

# 5. Initialize a variable `increment` to 1.
increment = 1

# 6. While `increment` is less than or equal to 500000, do the following:
while increment <= 500000:
    # Check if the element at `isAvailable[index]` is `True`.
    if isAvailable[index]:
        # If it is `True`, set `isAvailable[index]` to `False`.
        isAvailable[index] = False
    
    # Increase `increment` by 1.
    increment += 1
    
    # Update `index` to be the result of `(index + increment) mod numberOfElements`.
    index = (index + increment) % numberOfElements

# 7. Create a new list `remainingTrue` that includes all elements in `isAvailable` that are still `True`.
remainingTrue = [value for value in isAvailable if value]

# 8. If the length of `remainingTrue` is equal to 0, then:
if len(remainingTrue) == 0:
    # 9. Output 'YES'.
    print('YES')
# 10. Otherwise, output 'NO'.
else:
    print('NO')
# (End of program)
