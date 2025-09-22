def main():
    # Step 1: Receive Input
    first_list = input()  # First list of values as a string
    second_list = input()  # Second list of values as a string

    # Step 2: Split Input into Lists
    first_elements = first_list.split()  # Split the first list string into elements
    second_elements = second_list.split()  # Split the second list string into elements

    # Step 3: Initialize a Counter
    difference_count = 0  # Initialize the counter for differences

    # Step 4: Compare Corresponding Elements
    for index in range(3):  # Only compare the first three elements
        # Retrieve the current values and convert them to integers
        current_first_value = int(first_elements[index])  
        current_second_value = int(second_elements[index])  
        
        # Check if values are different
        if current_first_value != current_second_value:
            difference_count += 1  # Increment the counter if they are different

    # Step 5: Check Number of Differences and Output Result
    if difference_count < 3:
        print("YES")  # Less than 3 differences
    else:
        print("NO")  # 3 or more differences

# Invoke the main function to begin execution
main()
