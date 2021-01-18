# W3C validator for Holberton School

For HTML and CSS and SVG files

Levarages the W3C [Nu Html Checker](https://validator.github.io/)

## Installation
1. Clone this repo
```
git clone https://github.com/holbertonschool/W3C-Validator.git
```

2. Run shell script (see example in [usage](#usage) section below)

## Usage:

Simple file:

```
./w3c_validator.py index.html
```

Multiple files:

```
./w3c_validator.py index.html header.html styles/common.css
```

All errors are printed in `STDERR`; Exit status = # of errors (0 on success)