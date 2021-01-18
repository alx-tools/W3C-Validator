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