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


def check_file_extension(file):
    """Check for valid file extensions and return a boolean"""
    return file.endswith(".css") or file.endswith(
        ".html") or file.endswith(".svg")


def check_files():
    """Checks that arguments contain proper files"""
    for file in sys.argv[1:]:
        try:
            if not check_file_extension(file):
                raise ValueError
        except ValueError:
            sys.exit(
                "No files with a valid extension found.\n"
                "Files should end with '.html', '.css' or '.svg'")

def run(options="--errors-only"):
    """
    Collect arguments, check for Operating System and execute
    binaries
    """
    arguments = " ".join(sys.argv[1:])
    current_os = check_os()
    process = subprocess.Popen([current_os, options, arguments])
    process.wait()


def check_os():
    """
    Check Operating System and return proper path to binary
    """
    operating_system = platform.system()
    if operating_system == "Linux":
        return './lib/linux-vnu-runtime-image/bin/vnu'
    elif operating_system == "Darwin":
        return './lib/macos-vnu-runtime-image/bin/vnu'
    elif operating_system == "Windows":
        return './lib/windows-vnu-runtime-image/bin/vnu'
    else:
        sys.exit("OS could not be detected. Check requirements in README file")

