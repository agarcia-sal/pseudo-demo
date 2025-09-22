def do_main():
    # Step 1: Read two input strings
    input_1 = input()
    input_2 = input()

    # Step 2: Split the input strings into lists of words
    list_1 = input_1.split()
    list_2 = input_2.split()

    # Initialize result counter for mismatches
    mismatch_count = 0 

    # Step 3: Compare corresponding elements in both lists
    for index in range(3):  # We assume there are exactly three integers
        # Convert inputs to integers
        num1 = int(list_1[index])
        num2 = int(list_2[index])
        
        # Step 4: Count mismatches
        if num1 != num2:
            mismatch_count += 1 

    # Step 5: Determine result based on count of mismatches
    if mismatch_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    do_main()
