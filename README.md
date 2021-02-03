# W3C validator for Holberton School
For HTML, XHTML, SVG and CSS files

Based on 1 API:
- [Markup Validator Web Service API](https://validator.w3.org/docs/api.html)

## Requirements
- [Python 3](https://www.python.org/downloads/)
- [Requests: HTTP for Humans™](https://requests.readthedocs.io/en/master/index.html)

You can install Requests using pip:
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

## Usage

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
