======================
# TYT Download Automator
======================

TYT Download Automator automates the processs of downloading new episodes for members of the TYT Network


* Free software: MIT license


# Usage

Install the dependencies
```bash
$ pip install -r requirements.txt
```

Run all of the tests
```bash
$ tox
```

Run the tests just covering the functionality of the code i.e. not the style or the formatting
```bash
$ tox -e py36
```

Check formatting and style
```bash
$ tox -e flake8
```

Run the project as a module via
```bash
$ python -m tyt_download_automator
```

# Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and a custom project template.

