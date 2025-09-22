def read_input():
    """Read input from standard input and strip leading/trailing spaces."""
    return input().strip()

def normalize_path(input_path):
    """Normalize the path to ensure it follows POSIX conventions."""
    # This is a placeholder for normalization logic.
    # In a real scenario, you might want to use os.path.normpath or similar.
    normalized_path = input_path.replace('\\', '/')  # Convert backslashes to slashes
    return normalized_path

def remove_leading_slashes(path):
    """Remove leading slashes from the path, leaving only a single leading slash if present."""
    # This will replace multiple leading slashes with a single slash.
    return '/' + path.lstrip('/')

def main():
    """Main function to execute the path normalization process."""
    # Read input and normalize the path
    normalized_path = normalize_path(read_input())
    
    # Remove leading slashes
    output_path = remove_leading_slashes(normalized_path)
    
    # Print the final output path
    print(output_path)

if __name__ == "__main__":
    main()
