#!/bin/bash

# Create the directory
mkdir -p ~/.usr_scripts/cryptography/
echo "Directory has been created at ~/.usr_scripts/cryptography/"

# Download the code
curl -o ~/.usr_scripts/cryptography/encrypt_file.py https://raw.githubusercontent.com/AthomsG/cript/main/crypt.py
echo "Code has been pulled"

# Add the alias to the appropriate shell configuration file
if [[ $SHELL == *"bash"* ]]; then
    if ! grep -q "alias crypt=" ~/.bashrc; then
        echo "alias crypt='python3 ~/.usr_scripts/cryptography/encrypt_file.py'" >> ~/.bashrc
    fi
    source ~/.bashrc
elif [[ $SHELL == *"zsh"* ]]; then
    if ! grep -q "alias crypt=" ~/.zshrc; then
        echo "alias crypt='python3 ~/.usr_scripts/cryptography/encrypt_file.py'" >> ~/.zshrc
    fi
    source ~/.zshrc
fi

echo "Installation complete! Reset terminal and run 'crypt --help' for usage information, or check out the github repository: https://github.com/AthomsG/crypt/tree/main"

echo "Press any key to exit"
read -n 1
