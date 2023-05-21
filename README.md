# W3C validator for Holberton School
For HTML, CSS and SVG files

Based on 1 API:
- [Markup Validator Web Service API](https://validator.w3.org/docs/api.html)

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [Requests: HTTP for Humans™](https://requests.readthedocs.io/en/master/index.html)

## Quickstart
1. Clone this repo
```sh
git clone https://github.com/holbertonschool/W3C-Validator.git
```

2. Run the validator command from within

Single file:

```sh
./w3c_validator.py index.html
```

```sh
./w3c_validator.py css/styles.css
```

Multiple files:

```sh
./w3c_validator.py index.html article.html css/styles.css
```

All errors are printed in `STDERR`; Exit status = # of errors (0 on success)

# w3c_validator Installation and Usage Guide
This guide provides instructions on how to install and use the w3c_validator Python program. The w3c_validator is a tool that validates HTML files against the W3C HTML specification.
## Installation
To install the w3c_validator, follow these steps:
1. Ensure that Python 3 is installed on your system. You can verify this by running the command ``python3 --version`` in your terminal.
2. Clone this repo
```sh
git clone https://github.com/holbertonschool/W3C-Validator.git
```
3. Navigate to the repo folder on your system
4. Run the installation script by executing the following command:
```sh
sudo ./install.sh
```
Note: The installation script requires root privileges to move the necessary files to the appropriate system directory. You will be prompted to enter your password.


The installation script will move the "w3c_validator.py" and "w3c_validator" files to the "/usr/bin" directory, making the w3c_validator script accessible from any location.

5. installation complete

## Usage
To use the w3c_validator run: ``w3c_validator file [files]``
Example:
```sh
w3c_validator index.html
```
Multiple files:
```sh
w3c_validator index.html style.css register.html
```

```sh
./w3c_validator index.html article.html css/styles.css
```


## Troubleshooting
- If you encounter any issues during the installation or usage of the w3c_validator, please ensure that you have followed the installation steps correctly and have the necessary dependencies installed.


- Error: `bad interpreter: No such file or directory`
If you get this error you might not have Python installed correctly; or the system [PATH](https://en.wikipedia.org/wiki/PATH_(variable)) might not be updated to reflect the installed Python version.

Assuming that Python 3 is indeed installed, you can try to run it like so:
```
python3 w3c_validator.py index.html
```
- Error: `ModuleNotFoundError: No module named 'requests'`
If you get this error you do not have the module `requests` installed in your system.

You can install `requests` using pip:
```
python3 -m pip install requests
```

- If you still experience problems, refer to the official repository or source for any known issues, bug reports, or support documentation.