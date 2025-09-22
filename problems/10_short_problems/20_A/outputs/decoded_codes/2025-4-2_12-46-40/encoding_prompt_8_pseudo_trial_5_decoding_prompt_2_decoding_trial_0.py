import os

def main():
    # Step 1: Read the input from the user, trimming any extra spaces
    input_path = input().strip()
    
    # Step 2: Normalize the file path using os.path.normpath
    normalized_path = os.path.normpath(input_path)
    
    # Step 3: Adjust the path to ensure only one leading slash
    # This checks if the normalized path starts with a leading slash
    if normalized_path.startswith('/'):
        # Replace multiple leading slashes with a single slash
        output_path = '/' + normalized_path.lstrip('/')
    else:
        output_path = normalized_path.lstrip('/')
    
    # Step 4: Print the result
    print(output_path)

# Call the main function to execute
if __name__ == "__main__":
    main()
