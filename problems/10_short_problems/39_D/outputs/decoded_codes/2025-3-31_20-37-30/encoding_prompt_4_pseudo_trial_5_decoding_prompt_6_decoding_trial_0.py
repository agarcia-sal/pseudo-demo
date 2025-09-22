def do_main():
    # Read input values
    input1 = input()  # First line of input
    input2 = input()  # Second line of input
    
    # Split input strings into lists
    list1 = input1.split()  # Split the first input into words
    list2 = input2.split()  # Split the second input into words
    
    # Initialize the result counter for mismatches
    mismatch_count = 0

    # Compare corresponding elements in both lists
    for index in range(3):  # Loop from 0 to 2
        value1 = int(list1[index])  # Convert the corresponding element from list1 to integer
        value2 = int(list2[index])  # Convert the corresponding element from list2 to integer
        
        # Check if the values are not equal
        if value1 != value2:
            mismatch_count += 1  # Increment mismatch count if they are different
    
    # Determine if the number of mismatches is less than 3
    if mismatch_count < 3:
        print("YES")  # Print "YES" if mismatches are less than 3
    else:
        print("NO")   # Print "NO" otherwise

# Main entry point
do_main()  # Call the main function to execute
