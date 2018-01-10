# TYT Download Automator

TYT Download Automator automates the process of downloading new episodes for members of the TYT Network

## Why
The Young Turks (TYT) is a web-only news network that produces shows on a variety of topics (politics, sports, pop culture, etc). The main show is a live two-hour stream on YouTube covering news stories from the day with an emphasis on politics. After the show airs, a selection of news stories from the main show are posted to YouTube for anyone to see. For paying subscribers to their network, TYT provides commerical-free downloads of the entire main show, along with downloads of several other shows and podcasts.

I made this package to make my life a little easier. Sure, I could download, move, and rename all of the shows manually, but that's too tedious for my tastes. I also wanted an excuse to play around with Selenium.

I use this package to download the shows, rename them to something sensible, and store them in a Plex-compatible folder structure. Then, having downloaded the shows to the desktop in my bedroom, I can stream the shows to the TV in my living room without commercials.

* Free software: MIT license
* Disclaimer: I am in no way affiliated with The Young Turks or TYT Network

## Usage

#### System Requirements
* `tyt_download_automator` requires Python 3.6+
* `geckodriver` must be installed (explained below)

#### Download and install `tyt_download_automator`
You can do this by cloning the repository:

```bash
$ git clone https://github.com/zmitchell/tyt_download_automator.git
```

or by just downloading the ZIP archive. It doesn't really matter where you download `tyt_download_automator`.

The next step is to actually install `tyt_download_automator`, which will download the other Python libraries it depends on and install itself to your `site-packages` directory. `cd` into the `tyt_download_automator` folder and do the following:

```bash
$ python setup.py install
```

You'll also need [geckodriver](https://github.com/mozilla/geckodriver/releases), which is basically a version of Firefox meant to be used in automation and UI testing. You'll need to make sure that the `geckodriver` executable is in your `PATH`. It's very easy to do this, and you can find instructions with a quick search.

#### Login credentials
You need to be a member of the TYT Network in order to have access to the downloadable content. `tyt_download_automator` pretends to be you when it downloads the shows, so it needs you to store your login credentials in a way that it can read them, specifically as environment variables:

```bash
$ export TYT_USERNAME="mr_jackpots"
$ export TYT_PASSWORD="hunter12"
```

#### Download folder
The next step is tellling `tyt_download_automator` where to store the shows that it downloads. This is also set with an environment variable:

```bash
$ export TYT_DOWNLOAD_FOLDER="/path/to/folder"
```

The downloads will be stored in the following structure:
```text
/path/to/folder/YYYY-MM-DD/YYYY-MM-DD - <show name>.mp4
```

So, if you choose `/foo` as your download folder, you would see the following folder structure:
```text
/foo/2018-01-08/2018-01-08 - TYT Hour 1.mp4
/foo/2018-01-08/2018-01-08 - TYT Hour 2.mp4
/foo/2018-01-09/2018-01-09 - TYT Hour 1.mp4
/foo/2018-01-09/2018-01-09 - TYT Hour 2.mp4
...
```

#### Running `tyt_download_automator`

Since you've installed `tyt_download_automator` you can run the project from anywhere via
```bash
$ python -m tyt_download_automator
```

`tyt_download_automator` will open a new Firefox window, navigate to the TYT Network homepage, log you in, and start downloading the episodes on the front page. Every few minutes it will check for new episodes and download the ones you haven't already downloaded.

If it's the first time you've used the program (or if it's been a while) the program will crash because Firefox will try to install updates when it launches. This is a known issue, and I'm working on it. For now, all you have to do is launch the program again.

## Plans for the future
* Fix the crash on first launch
* Allow a user configurable polling interval
* Allow the user to select which shows they want to download, rather than downloading all of them
* More gracefully handle quitting the program with Ctrl-C

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and a custom project template.

