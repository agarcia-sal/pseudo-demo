def main():
    # Step 2: Receive Input
    first_input = input()
    second_input = input()

    # Step 3: Split Inputs
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 4: Initialize Difference Counter
    difference_count = 0

    # Step 5: Compare Corresponding Elements
    for index in range(3):  # Looping from 0 to 2 inclusive
        first_value = int(first_list[index])  # Convert to integer
        second_value = int(second_list[index])  # Convert to integer

        if first_value != second_value:  # Check for inequality
            difference_count += 1  # Increment the counter if values are different

    # Step 6: Determine Output
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Step 7: Execute Main Function
if __name__ == "__main__":
    main()
