# Main function to compare two sets of values
def compare_values():
    # Step 1: Input values
    t1 = input()  # Input first set of values as a string
    t2 = input()  # Input second set of values as a string
    
    # Step 2: Split input strings into lists
    tt1 = t1.split()  # Split t1 into a list of strings
    tt2 = t2.split()  # Split t2 into a list of strings
    
    # Initialize the result variable to count differences
    result_count = 0
    
    # Step 3: Compare values
    for x in range(3):  # Loop through each index
        # Step 3a: Convert string values to integers
        a = int(tt1[x])  # Convert the first list value to integer
        b = int(tt2[x])  # Convert the second list value to integer
        
        # Step 3b: Check for inequality
        if a != b:  # If the two values are not equal
            result_count += 1  # Increment the difference count
    
    # Step 4: Determine result based on inequality count
    if result_count < 3:  # If the count of differences is less than 3
        print("YES")  # Print YES if less than 3 differences
    else:
        print("NO")   # Print NO if 3 or more differences

# Call the function to execute
compare_values()
