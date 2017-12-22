======================
# TYT Download Automator
======================

TYT Download Automator automates the process of downloading new episodes for members of the TYT Network

I made this package to make my life a little easier. The Young Turks provide commerical-free downloads of their shows soon after they've aired. I use Plex to store these shows on a desktop, then stream them to the TV in my living room. The goal of this project is to automate the process of downloading new episodes, renaming them, and storing them in the correct folder structure.

* Free software: MIT license


# Usage

Before using this package, you'll need to add a file `tyt_download_automator/config.py`, which contains your login information and download location:

```python
# config.py
username = "myusername"
password = "mypassword"
download_folder = "/path/to/download/folder"
```

At some point this may change to reading environment variables for ease of use.

Run the project as a module via
```bash
$ python -m tyt_download_automator
```

# Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and a custom project template.

