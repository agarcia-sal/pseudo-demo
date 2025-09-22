def main():
    # Step 1: Read input from the user
    input_string_1 = input()
    input_string_2 = input()

    # Step 2: Split the input strings into lists of strings
    tokens_1 = input_string_1.split()
    tokens_2 = input_string_2.split()

    # Step 3: Initialize a counter for the differences
    difference_count = 0

    # Step 4: Compare the first three entries of both lists
    for index in range(3):
        value_from_first_input = int(tokens_1[index])
        value_from_second_input = int(tokens_2[index])

        # Increment the difference count if the values are not equal
        if value_from_first_input != value_from_second_input:
            difference_count += 1

    # Step 5: Output "YES" if differences are less than 3, else "NO"
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the code
main()
