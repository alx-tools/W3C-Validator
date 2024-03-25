# W3C validator for Holberton School
> This program is designed to validate `.HTML`, `.CSS`, and `.SVG` files. It checks these files for compliance with [W3C](https://www.w3.org/) standards, helping to ensure that your web content is accessible, reliable, and follows established web standards. This is crucial for maintaining compatibility across various web browsers and platforms. By using this program, developers can catch and fix errors early in the development process, improving the quality of their code and potentially saving time and resources.

## Table of Contents
 - [Requirements](#requirements)
 - [Usage](#quickstart)
 - [Troubleshooting](#troubleshooting)
 - [Contributing](#contributing)

---

#### Based on 1 API:
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

## Troubleshooting

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

If you don't have `pip` installed, you can get it [here](https://pypi.org/project/pip/).

## Contributing

To contribute to this project, follow these steps:
  * Fork this repository.
  * Create a branch: `git checkout -b <branch_name>`.
  * Make your changes and commit them: `git commit -m '<commit_message>'`.
  * Push to the original branch: `git push`
  * Create the pull request.

Alternatively see the Github documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).