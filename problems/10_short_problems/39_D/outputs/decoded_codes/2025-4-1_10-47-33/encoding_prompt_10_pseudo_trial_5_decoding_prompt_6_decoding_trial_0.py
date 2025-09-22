def do_main():
    # Declare input variables as strings
    first_line = ""
    second_line = ""
    
    # Initialize result variable
    result_count = 0

    # Read two lines of numbers from the user
    first_line = input()
    second_line = input()

    # Split the input strings into lists of strings
    first_numbers = first_line.split()
    second_numbers = second_line.split()

    # Iterate through the first three elements
    for index in range(3):
        # Convert the string values to integers
        number_a = int(first_numbers[index])
        number_b = int(second_numbers[index])
        
        # Check if the numbers are not equal
        if number_a != number_b:
            # Increment the count if they are not equal
            result_count += 1

    # Check how many numbers were not equal
    if result_count < 3:
        print("YES")
    else:
        print("NO")

# Call the main function if this file is executed
if __name__ == "__main__":
    do_main()
