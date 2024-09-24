import argparse
import os
import sys


def find_exe_files(directory):
    """
    Find all files with .exe extension in the given directory.

    Args:
        directory (str): The directory to search for .exe files.

    Returns:
        list: A list of paths to .exe files.
    """
    exe_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".exe"):
                exe_files.append(os.path.join(root, file))
    return exe_files


def delete_exe_files(exe_files):
    """
    Delete the specified .exe files.

    Args:
        exe_files (list): A list of .exe file paths to delete.
    """
    for file_path in exe_files:
        os.remove(file_path)
        print(f"Deleted: {file_path}")


def main():
    """
    Main function to handle argument parsing and orchestrate finding and deletion of .exe files.
    """
    parser = argparse.ArgumentParser(
        description="Delete .exe files from a specified directory with user confirmation."
    )
    parser.add_argument(
        "directory", type=str, help="The directory to delete .exe files from."
    )
    args = parser.parse_args()

    exe_files = find_exe_files(args.directory)

    if not exe_files:
        print("No .exe files found.")
        sys.exit(0)

    print(f"Found {len(exe_files)} .exe files.")
    print_list = (
        input("Do you want to print the list of .exe files? (yes/no): ").strip().lower()
        == "yes"
    )
    if print_list:
        for file in exe_files:
            print(file)

    confirm = (
        input("Are you sure you want to delete all these files? (yes/no): ")
        .strip()
        .lower()
        == "yes"
    )
    if confirm:
        delete_exe_files(exe_files)
        print(f"Total .exe files deleted: {len(exe_files)}")
    else:
        print("Deletion cancelled.")


if __name__ == "__main__":
    main()
