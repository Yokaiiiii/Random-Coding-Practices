import os
import shutil


def createFolderIfNeeded(folder_name, directory):
    """
    Creates a folder if it doesn't already exist.

    Parameters:
    folder_name (str): The name of the folder to create.
    directory (str): The directory in which to create the folder.

    Returns:
    str: The path to the created or existing folder.
    """
    folder_path = os.path.join(directory, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def moveFileToFolder(source, destination):
    """
    Moves a file to the specified destination folder.

    Parameters:
    source (str): The path to the source file.
    destination (str): The path to the destination folder.
    """
    shutil.move(source, destination)


def cleanFolder(directory):
    """
    Cleans the specified directory by moving files into folders based on their file types.

    Parameters:
    directory (str): The directory to clean.
    """
    for file in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, file)

        # Check if the item is a file
        if os.path.isfile(file_path):
            # Get file extension without the dot
            file_type = os.path.splitext(file)[1][1:]
            folder_name = f"{file_type.upper()}_Folder"

            # Create the folder if it doesn't exist
            destination = createFolderIfNeeded(folder_name, directory)

            # Move the file to the respective folder
            moveFileToFolder(file_path, destination)
            print(f"Moved {file} to {destination}")


def main():
    """
    Main function to execute the folder cleaning script.
    """
    print("Desktop Cleaner Script")
    directory = "C:/Users/Yokai/Desktop/DesktopClear"

    # Check if the directory exists
    if os.path.isdir(directory):
        cleanFolder(directory)
        print("Cleaning complete.")
    else:
        print("Invalid folder path. Please ensure the path is correct and try again")


# Execute the main function
main()
