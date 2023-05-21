#!/usr/bin/env bash
# This script installs the w3c_validator python script by moving the
# w3c_validator.py and w3c_validator to the /usr/bin folder
# so that the w3c_validator script can be executed from anywhere.

# Check if the script is executed with root privileges
if [[ $EUID -ne 0 ]]; then
    echo "Error: This script must be run with root privileges."
    exit 1
fi

# Move w3c_validator.py and w3c_validator to /usr/bin
mv "./w3c_validator.py" "/usr/bin"
mv "./w3c_validator" "/usr/bin"

echo "Installation complete. To use the w3c_validator, simply run the command:"
echo "w3c_validator file [files]"
