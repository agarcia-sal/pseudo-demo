def main():
    # Step 2: Get Inputs
    first_input = input()
    second_input = input()

    # Step 3: Split Inputs
    first_list = first_input.split()
    second_list = second_input.split()

    # Step 4: Initialize a Mismatch Counter
    mismatch_count = 0

    # Step 5: Compare Values
    for index in range(3):  # Loop from 0 to 2 inclusive
        first_value = int(first_list[index])
        second_value = int(second_list[index])
        
        if first_value != second_value:
            mismatch_count += 1

    # Step 6: Check Mismatch Count
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Step 8: Execute Main Function on Program Start
if __name__ == "__main__":
    main()
