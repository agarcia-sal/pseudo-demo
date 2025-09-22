# Function to read input data and remove leading/trailing spaces
def read_input():
    return input().strip()

# Function to normalize the path by removing redundant separators
def normalize_path(input_path):
    # Here, we will use a simplistic normalization assuming just as an example
    # This could include more complex logic depending on the requirements
    parts = input_path.split('/')
    normalized_parts = [part for part in parts if part]  # Remove empty parts
    return '/'.join(normalized_parts)

# Function to format the path by removing leading slashes
def format_path(normalized_path):
    # Return normalized path without leading slashes
    return normalized_path.lstrip('/')

# Main execution flow
def main():
    # Step 1: Read input path
    input_path = read_input()

    # Step 2: Normalize the path
    normalized_path = normalize_path(input_path)

    # Step 3: Format the path
    formatted_path = format_path(normalized_path)

    # Step 4: Output the final formatted path
    print(formatted_path)

# Call the main function to execute the program
main()
