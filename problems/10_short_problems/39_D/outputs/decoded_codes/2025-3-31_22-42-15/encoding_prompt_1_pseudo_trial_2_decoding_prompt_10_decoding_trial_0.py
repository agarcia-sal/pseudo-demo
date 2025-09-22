def doMain():
    # Step 2: Get Input Values
    first_input = input()  # First set of input values
    second_input = input()  # Second set of input values

    # Step 3: Split Input into Lists
    first_values = first_input.split()  # List of values from the first input
    second_values = second_input.split()  # List of values from the second input

    # Step 4: Initialize Difference Counter
    difference_count = 0  # Counter for differences

    # Step 5: Iterate and Count Differences
    for index in range(3):  # Iterate through the first three indices
        value_a = int(first_values[index])  # Convert first value to integer
        value_b = int(second_values[index])  # Convert second value to integer
        
        # Count the differences
        if value_a != value_b:
            difference_count += 1

    # Step 6: Decide Output Based on Count
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Run Main Function if Script is Executed
if __name__ == "__main__":
    doMain()
