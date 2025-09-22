def main():
    # Read first input string representing a series of values
    FIRST_INPUT = input()
    # Read second input string representing another series of values
    SECOND_INPUT = input()

    # Split the input strings into lists of strings
    FIRST_VALUES = FIRST_INPUT.split()
    SECOND_VALUES = SECOND_INPUT.split()

    # Initialize a variable to count differences
    DIFFERENCE_COUNT = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers for comparison
        FIRST_VALUE = int(FIRST_VALUES[index])
        SECOND_VALUE = int(SECOND_VALUES[index])
        
        # Compare the current elements from both lists
        if FIRST_VALUE != SECOND_VALUE:
            # Increment the difference count
            DIFFERENCE_COUNT += 1 

    # Check if the count of differences is less than 3
    if DIFFERENCE_COUNT < 3:
        # Print "YES" if there are less than 3 differences
        print("YES")
    else:
        # Print "NO" if there are 3 or more differences
        print("NO")

# Execute the main function
main()
