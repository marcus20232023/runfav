import os
import subprocess

def install_fzf():
    print("Installing fzf...")
    subprocess.run(["git", "clone", "--depth", "1", "https://github.com/junegunn/fzf.git", "~/.fzf"])
    subprocess.run(["~/.fzf/install", "--all"])

def add_to_bashrc():
    bashrc_path = os.path.expanduser("~/.bashrc")
    runfav_function = '''
#Favorite commands to run
runfav() {
  cmd=$(cat ~/.fav_commands | fzf)

  # Display and allow inline editing
  read -e -p "Command to run (edit if needed): " -i "$cmd" edited_cmd

  # Execute the edited command
  eval "$edited_cmd"
}
'''
    with open(bashrc_path, "a") as bashrc:
        bashrc.write(runfav_function)
    print("Added runfav function to .bashrc")

def create_fav_commands():
    fav_commands_path = os.path.expanduser("~/.fav_commands")
    if not os.path.exists(fav_commands_path):
        with open(fav_commands_path, "w") as f:
            f.write("# Add your favorite commands here, one per line\n")
        print("Created .fav_commands file")
    else:
        print(".fav_commands file already exists")

def main():
    install_fzf()
    add_to_bashrc()
    create_fav_commands()
    print("Setup complete. Please restart your terminal or run 'source ~/.bashrc' to use the new function.")

if __name__ == "__main__":
    main()