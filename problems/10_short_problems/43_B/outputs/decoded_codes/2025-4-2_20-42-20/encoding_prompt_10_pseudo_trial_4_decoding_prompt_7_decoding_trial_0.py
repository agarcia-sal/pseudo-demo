# Function to filter out spaces and create a list of characters from a string
def filtered_list(string):
    # Return a list of characters excluding spaces
    return [char for char in string if char != ' ']

# Main program logic
def main():
    # Step 1: Collect two lines of input
    first_input = input()
    second_input = input()

    # Step 2: Create a list of characters from the first input excluding spaces
    filtered_first = filtered_list(first_input)
    
    # Step 3: Create a list of characters from the second input excluding spaces
    filtered_second = filtered_list(second_input)

    # Step 4: Initialize frequency differences list
    frequency_differences = []

    # Step 5: Calculate frequency differences for ASCII characters from 'A' to 'z'
    # ASCII values from 65 (A) to 122 (z)
    for character_code in range(65, 123):
        character = chr(character_code)
        difference = filtered_first.count(character) - filtered_second.count(character)
        frequency_differences.append(difference)

    # Step 6: Check if any frequency difference is negative
    if any(diff < 0 for diff in frequency_differences):
        print("NO")
    else:
        print("YES")

# Call the main function to execute the program
main()
