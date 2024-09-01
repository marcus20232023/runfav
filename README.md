# RunFav

RunFav is a simple utility that allows you to quickly access and run your favorite commands using fuzzy search.

## Features

- Installs fzf (fuzzy finder) for easy command selection
- Adds a `runfav` function to your `.bashrc`
- Creates a `.fav_commands` file to store your favorite commands
- Allows inline editing of commands before execution

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

3. Use fuzzy search to find the command you want to run.

4. The selected command will be displayed for editing. Press Enter to run it as-is, or edit it before running.

## Requirements

- Python 3
- git
- Unix-like environment (Linux or macOS)

## Note

This script modifies your `.bashrc` file and installs fzf in your home directory. Make sure you understand these changes before running the script.

## License

[MIT License](https://opensource.org/licenses/MIT)