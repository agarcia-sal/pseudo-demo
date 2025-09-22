# 1. Begin the program (implicit in Python, just start defining the script)

# 2. Read an integer value `n` from user input
n = int(input())

# 3. Create a list `isActive` of length `n`, where all elements are initially set to `True`
isActive = [True] * n

# 4. Initialize a variable `currentIndex` to 0
currentIndex = 0

# 5. Initialize a variable `increment` to 1
increment = 1

# 6. While `increment` is less than or equal to 500000, do the following:
while increment <= 500000:
    # 1. If the element at `currentIndex` in the list `isActive` is `True`, then:
    if isActive[currentIndex]:
        # Set the element at `currentIndex` in the list `isActive` to `False`
        isActive[currentIndex] = False
        
    # 2. Increment `increment` by 1
    increment += 1
    
    # 3. Update `currentIndex` to be the sum of `currentIndex` and `increment`, then find the remainder when divided by `n`
    currentIndex = (currentIndex + increment) % n

# 7. Create a list `activeElements` that contains only the elements from `isActive` that are still `True`
activeElements = [value for value in isActive if value]

# 8. If the length of `activeElements` is equal to 0:
if len(activeElements) == 0:
    # Output "YES"
    print("YES")
# 9. Otherwise:
else:
    # Output "NO"
    print("NO")

# 10. End the program (implicit in Python, end of script)
