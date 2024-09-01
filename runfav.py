import os
import subprocess
import shutil
from datetime import datetime

def install_fzf():
    print("Installing fzf...")
    subprocess.run(["git", "clone", "--depth", "1", "https://github.com/junegunn/fzf.git", "~/.fzf"])
    subprocess.run(["~/.fzf/install", "--all"])

def backup_bashrc():
    bashrc_path = os.path.expanduser("~/.bashrc")
    backup_path = f"{bashrc_path}.{datetime.now().strftime('%Y%m%d%H%M%S')}.bak"
    shutil.copy(bashrc_path, backup_path)
    print(f"Backup of .bashrc created at {backup_path}")
    return backup_path

def restore_bashrc(backup_path):
    bashrc_path = os.path.expanduser("~/.bashrc")
    shutil.copy(backup_path, bashrc_path)
    print(f".bashrc restored from {backup_path}")

def add_to_bashrc():
    bashrc_path = os.path.expanduser("~/.bashrc")
    runfav_function = '''
#Favorite commands to run
runfav() {
  echo "Choose an option:"
  echo "(A)dd a new command"
  echo "(U)se an existing command"
  echo "(R)emove changes"
  read -p "Enter your choice (A/U/R): " choice

  if [[ $choice == "A" || $choice == "a" ]]; then
    read -p "Enter the new command to add: " new_cmd
    echo "$new_cmd" >> ~/.fav_commands
    echo "Command added successfully!"
  elif [[ $choice == "U" || $choice == "u" ]]; then
    cmd=$(cat ~/.fav_commands | fzf)
    if [ -n "$cmd" ]; then
      read -e -p "Command to run (edit if needed): " -i "$cmd" edited_cmd
      eval "$edited_cmd"
    fi
  elif [[ $choice == "R" || $choice == "r" ]]; then
    read -p "Are you sure you want to remove the changes? (y/n): " confirm
    if [[ $confirm == "Y" || $confirm == "y" ]]; then
      restore_bashrc ~/.bashrc.bak
      rm -f ~/.fav_commands
      echo "Changes removed successfully!"
    else
      echo "Removal cancelled."
    fi
  else
    echo "Invalid choice. Please run 'runfav' again and choose A, U, or R."
  fi
}
'''

    # Remove any existing runfav function definitions
    with open(bashrc_path, "r") as file:
        lines = file.readlines()

    with open(bashrc_path, "w") as file:
        skip = False
        for line in lines:
            if line.strip() == "runfav() {":
                skip = True
            if not skip:
                file.write(line)
            if skip and line.strip() == "}":
                skip = False

    # Add the new runfav function definition
    with open(bashrc_path, "a") as file:
        file.write(runfav_function)

    print("Updated .bashrc with the new runfav function")

def create_fav_commands():
    fav_commands_path = os.path.expanduser("~/.fav_commands")
    if not os.path.exists(fav_commands_path):
        with open(fav_commands_path, "w") as f:
            f.write('''# Add your favorite commands here, one per line
find . -type f -name "*.txt" | xargs grep "search_term"
du -sh * | sort -hr | head -n 10
ps aux | sort -rk 3,3 | head -n 10
tar -czvf archive.tar.gz /path/to/directory
rsync -avz -e ssh /local/dir user@remote:/path/to/dir
awk '{print $1}' file.txt | sort | uniq -c | sort -nr
sed -i 's/old_text/new_text/g' file.txt
find . -type f -mtime -7 -print
netstat -tuln
ss -tuln
lsof -i :port_number
curl -s https://api.ipify.org
history | awk '{print $2}' | sort | uniq -c | sort -rn | head
df -h | grep -v tmpfs
free -h
top -b -n 1 | head -n 20
journalctl -p err..alert
last -n 20
w
who
''')
        print("Created .fav_commands file with 20 helpful commands")
    else:
        print(".fav_commands file already exists")

def main():
    backup_path = backup_bashrc()
    install_fzf()
    add_to_bashrc()
    create_fav_commands()
    print("Setup complete. Please restart your terminal or run 'source ~/.bashrc' to use the new function.")

if __name__ == "__main__":
    main()