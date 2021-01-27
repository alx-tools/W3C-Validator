# W3C validator for Holberton School

For HTML and CSS files.

Based on 2 APIs:

- https://validator.w3.org/nu/
- http://jigsaw.w3.org/css-validator/validator

## Requirements
[Python 3](https://www.python.org/downloads/)
[Requests: HTTP for Humans™](https://requests.readthedocs.io/en/master/index.html)

You can install requests using pip:
```
python 3 -m pip install requests
```

If you don't have pip installed, you can get it [here](https://pypi.org/project/pip/).

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
[The Nu Html Checker (v.Nu)](https://github.com/validator/validator)
[Nu Html Checker Checker output format](https://github.com/validator/validator/wiki/Output-%C2%BB-JSON)
