# 1. Start the program (implicit in Python code structure)

# 2. Input the total number of elements n.
n = int(input())

# 3. Create a list called isUnmarked with n elements, all initialized to True.
isUnmarked = [True] * n

# 4. Set variable currentIndex to 0.
currentIndex = 0

# 5. Set variable step to 1.
step = 1

# 6. While loop: Continue as long as step is less than or equal to 500,000:
while step <= 500000:
    # If isUnmarked[currentIndex] is True:
    if isUnmarked[currentIndex]:
        # Set isUnmarked[currentIndex] to False (mark it as processed).
        isUnmarked[currentIndex] = False

    # Increment step by 1.
    step += 1

    # Update currentIndex to (currentIndex + step) % n (wrap around the index if necessary).
    currentIndex = (currentIndex + step) % n

# 7. Create a new list called unmarkedIndices that contains all values from isUnmarked that are still True.
unmarkedIndices = [i for i in range(n) if isUnmarked[i]]

# 8. If the length of unmarkedIndices is 0:
if len(unmarkedIndices) == 0:
    # Output 'YES' (indicating all indices were marked).
    print('YES')
# 9. Else:
else:
    # Output 'NO' (indicating there are still unmarked indices).
    print('NO')

# 10. End the program (implicit in Python code structure)
