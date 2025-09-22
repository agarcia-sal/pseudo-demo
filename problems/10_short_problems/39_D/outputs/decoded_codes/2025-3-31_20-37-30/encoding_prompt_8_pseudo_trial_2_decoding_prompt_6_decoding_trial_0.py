def main():
    # Step 1: Get two strings of numbers from the user
    input_string1 = input()
    input_string2 = input()

    # Step 2: Split the input strings into individual numbers
    numbers_list1 = input_string1.split()
    numbers_list2 = input_string2.split()

    # Step 3: Initialize a counter for differences
    difference_count = 0

    # Step 4: Compare each corresponding number in the two lists
    for index in range(3):  # We assume exactly three numbers in each string
        number1 = int(numbers_list1[index])  # Convert to integer
        number2 = int(numbers_list2[index])  # Convert to integer

        # Step 5: Check if the numbers are different
        if number1 != number2:
            difference_count += 1  # Increment difference count

    # Step 6: Determine if the count of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Trigger the main function if the script is run directly
if __name__ == "__main__":
    main()
