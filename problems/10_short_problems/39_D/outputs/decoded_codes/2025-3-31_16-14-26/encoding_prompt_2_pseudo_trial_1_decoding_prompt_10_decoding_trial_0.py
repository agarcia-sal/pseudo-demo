def do_main():
    # Step 2: Prompt for User Input
    input_string1 = input()
    input_string2 = input()

    # Step 3: Process the Input
    list_of_values1 = input_string1.split()
    list_of_values2 = input_string2.split()

    # Step 4: Initialize a Counter
    difference_count = 0

    # Step 5: Compare Values
    for index in range(3):  # Compare only the first 3 corresponding values
        value_a = int(list_of_values1[index])  # Convert to integer
        value_b = int(list_of_values2[index])  # Convert to integer
        if value_a != value_b:  # Check for inequality
            difference_count += 1  # Increment count if values are different

    # Step 6: Output the Result
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Start the Program
if __name__ == "__main__":
    do_main()
