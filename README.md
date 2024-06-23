
# File Explorer Program

This simple file explorer program allows users to navigate directories, perform basic file and folder operations, view file information, and search for files or folders using a set of commands.

### Installation

Clone this repository to your local machine:
```sh
git clone https://github.com/Programming-Sai/File-Explorer.git
```

Navigate to the project directory:
```sh
cd  File-Explorer
```

Run the file explorer program:
```sh
python CLUI.py
```

## Features

1. **Navigation and Basic Commands**
   - **Display Contents**: Use the `.display` command to see the contents of the current directory.
   - **Navigate to Subdirectory**: Use the `.open_x` command, where `x` is the number associated with the subdirectory in the displayed contents, to navigate into a subdirectory.
   - **Go Back**: Use the `.back` command to move to the parent directory.

2. **File and Folder Operations**
   - **Delete**: Use the `.delete_x` command to delete a file or folder, replacing `x` with the corresponding number.
   - **Rename**: Use the `.rename_x` command to rename a file or folder, providing the new name when prompted.
   - **Create New Folder**: Use the `.new` command to create a new folder.

3. **View File Information**
   - **Get Info**: Use the `.info_x` command, replacing `x` with the corresponding number, to get information about a file or folder.

4. **Search for Files or Folders**
   - **Search**: Use the `.search` command to search for files or folders. Enter the search term when prompted, and the results will be displayed.

5. **Help and Exiting**
   - **Help**: Use the `.help` command for assistance or a reminder of available commands.
   - **Exit**: Use the `.exit` command to exit the program.

## Important Notes

- **File Deletion**: Be cautious with file deletion as it is permanent and cannot be undone. Confirm your actions before proceeding.
- **Command Accuracy**: Some commands require you to provide a number (e.g., `.delete_x`). Ensure you enter the correct number corresponding to the file or folder you want to operate on.
- **Frequent Display**: Use the `.display` command frequently to keep track of your current location and available files/folders.

## Additional Tips

- **Backup**: Backup important files before performing operations that could lead to data loss.
- **Experiment**: Experiment with the commands in a safe environment before using them on critical files.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine


### Usage

Once the program is running, you can use the following commands to interact with the file system:

- `.display`: Display the contents of the current directory.
- `.open_x`: Navigate to the subdirectory numbered `x`.
- `.back`: Go back to the parent directory.
- `.delete_x`: Delete the file or folder numbered `x`.
- `.rename_x`: Rename the file or folder numbered `x`.
- `.new`: Create a new folder.
- `.info_x`: Get information about the file or folder numbered `x`.
- `.search`: Search for files or folders.
- `.help`: Display the help information.
- `.exit`: Exit the program.
