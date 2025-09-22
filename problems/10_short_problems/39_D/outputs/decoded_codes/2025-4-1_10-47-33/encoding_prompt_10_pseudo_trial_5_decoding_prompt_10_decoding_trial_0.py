def main():
    # Declare variables
    first_input = ""
    second_input = ""
    discrepancy_count = 0

    # Get user input
    print("Please enter the first line of numbers:")
    first_input = input()
    print("Please enter the second line of numbers:")
    second_input = input()

    # Split the input into lists of strings
    first_numbers = first_input.split()
    second_numbers = second_input.split()

    # Iterate through the first three numbers in both lists
    for index in range(3):
        number_a = int(first_numbers[index])
        number_b = int(second_numbers[index])

        # Increment discrepancy count if numbers are not equal
        if number_a != number_b:
            discrepancy_count += 1

    # Output the result based on discrepancy count
    if discrepancy_count < 3:
        print("YES")
    else:
        print("NO")

# Ensure the script runs as the main program
if __name__ == "__main__":
    main()
