#!/usr/bin/python3
"""
W3C validator for Holberton School

For HTML, CSS and SVG files.

Makes use of the Nu Html Checker from the W3c.

Usage:

Simple file:

```
./w3c_validator.py index.html
```

Multiple files:

```
./w3c_validator.py index.html header.html styles/common.css
```

All errors are printed in `STDERR`

Return:
Exit status is the # of errors, 0 on Success

"""
import sys
import subprocess
import platform
import os


def check_file_extension(file):
    """Check for valid file extensions and return a boolean"""
    return file.endswith((".css", ".html", ".htm", ".svg"))


def check_files(files):
    """Checks that arguments contain proper files"""
    for file in files:
        try:
            if not os.path.isfile(file):
                raise IOError
            if not check_file_extension(file):
                raise ValueError
        except ValueError:
            sys.exit(
                "No files with a valid extension found.\n"
                "Files should end with '.html', 'htm', '.css' or '.svg'")
        except IOError:
            sys.exit(
                f"File {file} is not present in the current directory. Check file name and try again.")


def run(options):
    """
    Collect arguments, check for Operating System and execute
    binaries with options
    """
    options += " --also-check-css --skip-non-html --also-check-svg"
    files = " ".join(sys.argv[1:])
    current_os = check_os()
    process = subprocess.Popen([current_os, options, files])
    process.wait()


def check_os():
    """
    Check Operating System and return proper path to binary
    """
    operating_system = platform.system()
    binary_path = f"./lib/{operating_system}-vnu-runtime-image/bin/vnu"
    if operating_system == "Linux":
        return binary_path
    elif operating_system == "Darwin":
        return binary_path
    elif operating_system == "Windows":
        return binary_path
    else:
        sys.exit("OS could not be detected. Check requirements in README file")


if __name__ == "__main__":
    """Main"""
    error_message = "Usage: w3c_vallidatory.py index.html styles.css"
    if len(sys.argv) < 2:
        error_message = "Usage: w3c_vallidatory.py index.html styles.css"
        sys.exit(f"Not enough arguments provided\n{error_message}")
    check_files(sys.argv[1:])
    run()
