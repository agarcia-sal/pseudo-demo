def do_main():
    # Read input values
    input1 = input()
    input2 = input()
    
    # Split input strings into lists
    list1 = input1.split()
    list2 = input2.split()
    
    # Initialize the result counter for mismatches
    mismatch_count = 0

    # Compare corresponding elements in both lists
    for index in range(3):
        # Convert list elements to integers
        value1 = int(list1[index])
        value2 = int(list2[index])
        
        # Increment the mismatch count if the values are not equal
        if value1 != value2:
            mismatch_count += 1
        
    # Determine if the number of mismatches is less than 3
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")
        
# Main entry point
do_main()
