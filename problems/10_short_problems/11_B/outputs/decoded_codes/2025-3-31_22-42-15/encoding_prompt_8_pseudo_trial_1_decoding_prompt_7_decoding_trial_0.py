# Function to find the smallest non-negative integer whose triangular number
# matches or exceeds a given positive integer and checks the conditions
def find_triangular_index():
    # 1. Obtain a positive integer from the user
    targetValue = abs(int(input()))

    # 2. Initialize a variable 'currentIndex' to 0
    currentIndex = 0

    # 3. Begin an infinite loop to calculate triangular numbers
    while True:
        # a. Calculate the triangular number for 'currentIndex'
        triangularNumber = (currentIndex * (currentIndex + 1)) // 2  # Using integer division for safety

        # b. Calculate the difference between the triangular number and 'targetValue'
        difference = triangularNumber - targetValue

        # c. Check if the triangular number equals the targetValue
        if triangularNumber == targetValue:
            print(currentIndex)  # Print the currentIndex
            break  # Exit the loop

        # d. Check if the triangular number is greater than the targetValue
        if triangularNumber > targetValue:
            # Check if the difference is an even number
            if difference % 2 == 0:  # If remainder when divided by 2 equals 0
                print(currentIndex)  # Print the currentIndex
                break  # Exit the loop

        # e. Increment 'currentIndex' by 1 to check the next triangular number
        currentIndex += 1

# Calling the function to execute
find_triangular_index()
