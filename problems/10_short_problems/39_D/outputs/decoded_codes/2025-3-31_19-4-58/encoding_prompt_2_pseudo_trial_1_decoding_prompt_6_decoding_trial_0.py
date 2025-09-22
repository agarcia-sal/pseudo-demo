# Step 1: Start Main Function
def main():
    # Step 2: Get Inputs
    first_input = input()  # Storing first input
    second_input = input()  # Storing second input
    
    # Step 3: Split Inputs
    first_list = first_input.split()  # Splitting first input into a list of strings
    second_list = second_input.split()  # Splitting second input into a list of strings
    
    # Step 4: Initialize a Mismatch Counter
    mismatch_count = 0  # Starting the mismatch counter at zero

    # Step 5: Compare Values
    for index in range(3):  # Looping through first three indexes (0 to 2)
        first_value = int(first_list[index])  # Converting value from first list to integer
        second_value = int(second_list[index])  # Converting value from second list to integer
        # If the values do not match, increment the mismatch count
        if first_value != second_value:
            mismatch_count += 1
    
    # Step 6: Check Mismatch Count
    if mismatch_count < 3:
        print("YES")  # Output "YES" if mismatches are less than 3
    else:
        print("NO")  # Output "NO" if mismatches are 3 or more

# Step 8: Execute Main Function on Program Start
main()
