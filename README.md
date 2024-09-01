# RunFav

RunFav is a simple utility that allows you to quickly access and run your favorite commands using fuzzy search.

## Features

- Installs fzf (fuzzy finder) for easy command selection
- Adds a `runfav` function to your `.bashrc`
- Creates a `.fav_commands` file to store your favorite commands
- Allows inline editing of commands before execution
- Option to add new commands to the list
- Option to remove the changes and restore the original `.bashrc` file

## Installation

1. Ensure you have Python 3 and git installed on your system.

2. Clone this repository or download the `runfav.py` script.

3. Run the setup script:

   ```
   python3 runfav.py
   ```

4. Restart your terminal or run `source ~/.bashrc` to apply the changes.

## Usage

1. Add your favorite commands to the `~/.fav_commands` file, one command per line.

2. In your terminal, run:

   ```
   runfav
   ```

3. Choose an option:
   - `(A)dd a new command`: Add a new command to the `~/.fav_commands` file.
   - `(U)se an existing command`: Use fuzzy search to find and run a command from the `~/.fav_commands` file.
   - `(R)emove changes`: Restore the original `.bashrc` file and remove the `~/.fav_commands` file.

4. If you choose to use an existing command, the selected command will be displayed for editing. Press Enter to run it as-is, or edit it before running.

## Requirements

- Python 3
- git
- Unix-like environment (Linux or macOS)

## Note

This script modifies your `.bashrc` file and installs fzf in your home directory. Make sure you understand these changes before running the script. A backup of your `.bashrc` file will be created before any modifications.

## License

[MIT License](https://opensource.org/licenses/MIT)