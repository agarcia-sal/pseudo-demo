def main():
    # Step 1: Input the size of the array
    sizeOfArray = int(input())

    # Step 2: Initialize a list of boolean values
    isTrue = [True] * sizeOfArray

    # Step 3: Initialize counters
    index = 0
    step = 1

    # Step 4: Loop until step exceeds 500000
    while step <= 500000:
        # Step 4a: Check the current index in the boolean list
        if isTrue[index]:
            # Step 4b: Mark the current index as False
            isTrue[index] = False
        
        # Step 4c: Increment step
        step += 1

        # Step 4d: Calculate the next index using circular arithmetic
        index = (index + step) % sizeOfArray

    # Step 5: Filter the list to find remaining True values
    remainingTrueValues = [value for value in isTrue if value]

    # Step 6: Check if there are any True values left
    if len(remainingTrueValues) == 0:
        # Step 6a: If no True values are left, print 'YES'
        print('YES')
    else:
        # Step 6b: If there are True values left, print 'NO'
        print('NO')

# Since we're running the function, we should call it within the appropriate scope
if __name__ == "__main__":
    main()
