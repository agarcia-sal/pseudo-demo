def main():
    # Read input path from standard input and trim whitespace
    input_path = input().strip()  # Read and trim any surrounding whitespace
    normalized_path = normalize_path(input_path)
    
    # Print the normalized path
    print(normalized_path)

def normalize_path(input_path):
    # Normalize the path by removing redundant slashes
    trimmed_path = remove_leading_slashes(input_path)
    final_path = '/' + trimmed_path  # Ensure it starts with a single leading slash
    return final_path

# Helper function to remove leading slashes
def remove_leading_slashes(path):
    while path.startswith('/'):
        path = path[1:]  # Remove the leading slash
    return path

# Call main function to run the program
if __name__ == "__main__":
    main()
