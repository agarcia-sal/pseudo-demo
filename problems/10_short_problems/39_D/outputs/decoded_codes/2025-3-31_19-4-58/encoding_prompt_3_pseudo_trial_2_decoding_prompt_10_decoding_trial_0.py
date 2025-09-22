def main():
    # Step 1: Obtain inputs from the user
    first_input = input()  # First string of values
    second_input = input()  # Second string of values
    
    # Step 2: Split the input strings into lists of individual string values
    first_values = first_input.split()
    second_values = second_input.split()
    
    # Step 3: Initialize a counter for differences
    difference_count = 0
    
    # Step 4: Compare the values in the two lists
    for index in range(3):  # Comparing three pairs of values
        # Convert the values to integers
        value_a = int(first_values[index])
        value_b = int(second_values[index])
        
        # Step 5: Check if the two values are different
        if value_a != value_b:
            difference_count += 1

    # Step 6: Determine the result based on the count of differences
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Start the program execution
if __name__ == "__main__":
    main()
