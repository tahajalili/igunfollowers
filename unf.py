def read_unfollowers(file_path):
    """Read a list of unfollowers from a file, one username per line."""
    try:
        with open(file_path, 'r') as file:
            # Strip whitespace and filter out empty lines
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print(f"Warning: File {file_path} not found. Creating a new one.")
        # Create an empty file
        with open(file_path, 'w') as file:
            pass
        return set()

def save_unfollowers(file_path, unfollowers):
    """Save a list of unfollowers to a file, one username per line."""
    with open(file_path, 'w') as file:
        for username in sorted(unfollowers):
            file.write(f"{username}\n")

def find_new_unfollowers(old_file, new_file, output_file=None):
    """
    Compare two unfollower lists and identify the new unfollowers.
    
    Args:
        old_file: Path to the old unfollowers list file
        new_file: Path to the new unfollowers list file
        output_file: Path to save the new unfollowers (optional)
        
    Returns:
        set: The set of new unfollowers
    """
    old_unfollowers = read_unfollowers(old_file)
    new_unfollowers = read_unfollowers(new_file)``
    
    # Find unfollowers that are in the new list but not in the old list
    newly_unfollowed = new_unfollowers - old_unfollowers
    
    # Update the old list to include new unfollowers
    if output_file:
        combined_unfollowers = old_unfollowers.union(new_unfollowers)
        save_unfollowers(output_file, combined_unfollowers)
    
    return newly_unfollowed

def username_to_url(newly_unfollowed):
    if newly_unfollowed:
        return {f"https://www.instagram.com/{username}/" for username in newly_unfollowed}



def main():
    old_file = "old_unfollowers.txt"
    new_file = "new_unfollowers.txt"
    master_file = "master_unfollowers.txt"
    
    # Find new unfollowers and update the master list
    new_unfollowers = find_new_unfollowers(master_file, new_file, master_file)
    
    # Print results
    if new_unfollowers:
        print(f"Found {len(new_unfollowers)} new unfollower(s):")
        url = username_to_url(new_unfollowers)
        for url in sorted(urls):
            print(f" - {url}")
    else:
        print("No new unfollowers found.")
        
if __name__ == "__main__":
    main()
