def main():
    # Step 2.1: Receive Input
    first_list = input()  # Read the first list of values
    second_list = input()  # Read the second list of values

    # Step 2.2: Split Input into Lists
    first_elements = first_list.split()  # Split by spaces
    second_elements = second_list.split()  # Split by spaces

    # Step 2.3: Initialize a Counter
    difference_count = 0

    # Step 2.4: Compare Corresponding Elements
    for index in range(3):  # Assume there are at least 3 elements to compare
        current_first_value = int(first_elements[index])  # Convert to integer
        current_second_value = int(second_elements[index])  # Convert to integer
        
        if current_first_value != current_second_value:  # Compare values
            difference_count += 1  # Increment counter if values are different

    # Step 2.5: Check Number of Differences
    if difference_count < 3:
        print("YES")  # Output if differences are less than 3
    else:
        print("NO")  # Output if differences are 3 or more

# Step 3: Invoke Main Function to Begin Execution
if __name__ == "__main__":
    main()
