# Function to find the first non-negative integer index
# such that the sum of the first 'index' integers either 
# equals 'n' or the difference is even
def find_index():
    # Step 1: Initialize Input
    n = abs(int(input()))  # Get an absolute integer input value 'n'

    # Step 2: Set Initial Values
    index = 0  # Start index at 0

    # Step 3: Repeat Until Found (Infinite Loop)
    while True:
        # Step 4: Calculate Sum
        sumUpToIndex = (index * (index + 1)) // 2  # Use integer division to calculate sum

        # Step 5: Determine the Difference
        difference = sumUpToIndex - n

        # Step 6: Check for Equality
        if sumUpToIndex == n:
            print(index)  # Print the current 'index' if sum equals 'n'
            break  # Exit the loop

        # Step 7: Check for Greater Than Condition
        if sumUpToIndex > n:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the current 'index' if difference is even
                break  # Exit the loop

        # Step 8: Increment Index
        index += 1  # Increase index by 1 to check the next integer

# Call the function to execute
find_index()
