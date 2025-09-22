def read_input():
    # Step 1: Read input data
    return input().strip()  # Read the entire input and remove leading/trailing spaces

def normalize_path(input_path):
    # Step 2: Normalize the path
    # This is a simple implementation; in practice, you'd need to properly handle "..", ".", etc.
    parts = input_path.split('/')  # Split the path by '/'
    normalized_parts = []
    for part in parts:
        if part == '' or part == '.':
            continue  # Ignore empty parts and current directory references
        if part == '..':
            if normalized_parts:  # Only go up if there are parts to go up from
                normalized_parts.pop()  # Remove the last part to go up one level
        else:
            normalized_parts.append(part)  # Add the valid part to the normalized list
    return '/' + '/'.join(normalized_parts)  # Join back into a single path with leading slash

def format_path(normalized_path):
    # Step 3: Format the path
    return normalized_path.lstrip('/')  # Remove leading slashes to standardize the path

def main():
    # Step 4: Main execution flow
    input_path = read_input()  # Read input path
    normalized_path = normalize_path(input_path)  # Normalize the path
    formatted_path = format_path(normalized_path)  # Format the path
    print(formatted_path)  # Output the final formatted path

if __name__ == "__main__":
    main()  # Run the main function
