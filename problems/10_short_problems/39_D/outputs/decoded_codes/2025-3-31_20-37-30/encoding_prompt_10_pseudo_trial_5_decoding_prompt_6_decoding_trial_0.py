def do_main():
    # Step 1: Read two lines of input
    input1 = input()  # First line input
    input2 = input()  # Second line input

    # Step 2: Split the input strings into lists of strings
    list1 = input1.split()  # Split by space
    list2 = input2.split()  # Split by space
    
    # Step 3: Initialize a count for differences
    difference_count = 0

    # Step 4: Compare corresponding elements in the two lists
    for index in range(3):  # Loop for the first three elements
        # Step 4a: Convert string elements to integer
        value1 = int(list1[index])  # Convert first list element to integer
        value2 = int(list2[index])  # Convert second list element to integer

        # Step 4b: Check for differences
        if value1 != value2:  # If the values are not equal
            difference_count += 1  # Increment the difference count

    # Step 5: Check the count of differences and output the result
    if difference_count < 3:  # If differences are less than 3
        print("YES")
    else:
        print("NO")

# Main Execution Block
do_main()
