def do_main():
    # Read two strings of input
    input_string_1 = input()
    input_string_2 = input()

    # Split the input strings into lists of words
    words_list_1 = input_string_1.split()
    words_list_2 = input_string_2.split()

    # Initialize a counter for differences
    difference_count = 0 

    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the corresponding elements to integers
        number_a = int(words_list_1[index])
        number_b = int(words_list_2[index])

        # If the numbers are not the same, increment the difference counter
        if number_a != number_b:
            difference_count += 1 

    # Check if the number of differences is less than 3
    if difference_count < 3:
        print("YES")
    else:
        print("NO")

# Main execution block
if __name__ == "__main__":
    do_main()
