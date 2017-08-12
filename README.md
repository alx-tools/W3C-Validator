# W3C validator for Holberton School

For HTML and CSS files.

Based on 2 APIs:

- https://validator.w3.org/nu/
- http://jigsaw.w3.org/css-validator/validator

## Installation
1. Clone this repo
```sh
git clone https://github.com/holbertonschool/W3C-Validator.git
```

2. Run shell script (see example in [usage](#usage) section below)

## Usage:

Simple file:

```sh
./w3c_validator.py index.html
```

Multiple files:

```sh
./w3c_validator.py index.html header.html styles/common.css
```

All errors are printed in `STDERR`; Exit status = # of errors (0 on success)


## References

https://developer.mozilla.org/en-US/
