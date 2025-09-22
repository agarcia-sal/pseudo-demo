def main():
    # Step 1: Read input from the user
    user_input = input().strip()
    
    # Step 2: Initialize index and result variable
    index = 0
    result = ""

    # Step 3: Loop through the string until the end
    while index < len(user_input):
        # Step 4: Check for specific characters and update result
        if user_input[index] == '.':
            result += '0'
            index += 1
        elif index + 1 < len(user_input) and user_input[index + 1] == '.':
            result += '1'
            index += 2
        else:
            result += '2'
            index += 2

    # Step 5: Output the result
    print(result)

# Ensures that the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()
