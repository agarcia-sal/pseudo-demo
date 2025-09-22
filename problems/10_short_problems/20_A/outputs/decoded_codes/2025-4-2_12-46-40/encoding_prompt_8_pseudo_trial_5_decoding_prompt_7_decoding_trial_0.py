import os

def main():
    # Step 1: Read the input from the user
    # Read the entire input line and remove any extra spaces around it
    input_path = input().strip()
    
    # Step 2: Normalize the file path
    # Use os.path.normpath to normalize the input path according to POSIX standards
    normalized_path = os.path.normpath(input_path)

    # Step 3: Adjust the path
    # Replace any occurrence of multiple leading slashes with a single leading slash
    if normalized_path.startswith('/'):
        # Keep the first slash and replace any additional leading slashes with an empty string
        output_path = '/' + normalized_path.lstrip('/')
    else:
        # If there are no leading slashes, use the normalized path as is
        output_path = normalized_path

    # Step 4: Print the result
    # Display the final adjusted path to the user
    print(output_path)

# Call the main function to execute the script
if __name__ == "__main__":
    main()
