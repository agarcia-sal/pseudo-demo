def main():
    # Step 1: Obtain inputs from the user
    first_input = input()
    second_input = input()
    
    # Step 2: Split the input strings into lists of individual string values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare the values in the two lists
    for index in range(3):  # since we want to compare three pairs of values
        value_a = int(first_values[index])  # convert to integer
        value_b = int(second_values[index])  # convert to integer
        
        # Step 5: Check if the two values are different
        if value_a != value_b:
            difference_count += 1  # Increment difference counter

    # Step 6: Determine the result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Start the program execution
if __name__ == "__main__":
    main()
