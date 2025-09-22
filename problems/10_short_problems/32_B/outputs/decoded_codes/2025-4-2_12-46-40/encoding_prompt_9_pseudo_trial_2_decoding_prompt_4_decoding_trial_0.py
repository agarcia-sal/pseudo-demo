def main():
    # Step 2: Receive Input
    input_string = input().strip()

    # Step 3: Initialize Variables
    current_index = 0
    output_string = ""

    # Step 4: Process Input String
    while current_index < len(input_string):
        if input_string[current_index] == '.':
            output_string += '0'
            current_index += 1
        elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
            output_string += '1'
            current_index += 2
        else:
            output_string += '2'
            current_index += 2

    # Step 5: Output Result
    print(output_string)

# Entry point of the program
if __name__ == "__main__":
    main()
