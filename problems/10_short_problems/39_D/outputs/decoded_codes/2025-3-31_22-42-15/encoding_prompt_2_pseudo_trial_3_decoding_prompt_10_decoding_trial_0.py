def main():
    # Step 2: Obtain the first set of input values from the user.
    first_input = input()
    
    # Step 3: Obtain the second set of input values from the user.
    second_input = input()
    
    # Step 4: Split the inputs into lists of values.
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Step 6: Initialize a discrepancy count.
    discrepancy_count = 0
    
    # Step 7: Check values at indices 0, 1, and 2.
    for index in range(3):
        # Convert string values to integers.
        value_from_first = int(first_values[index])
        value_from_second = int(second_values[index])
        
        # Compare the two values.
        if value_from_first != value_from_second:
            discrepancy_count += 1

    # Step 8: Evaluate the discrepancy count and output the result.
    if discrepancy_count < 3:
        print("YES")
    else:
        print("NO")

# Step 1: Begin the main process.
if __name__ == "__main__":
    main()
